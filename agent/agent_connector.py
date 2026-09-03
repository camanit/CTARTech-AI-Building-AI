import argparse
import ast
import json
import os
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from pathlib import Path


def build_prompt(task):
    return (
        "You are a coding agent. Return only valid Python source code, without "
        f"explanation. Implement this task: {task}"
    )


def request_gemini(task, api_key, model, timeout):
    endpoint = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={api_key}"
    )
    payload = {"contents": [{"parts": [{"text": build_prompt(task)}]}]}
    request = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError) as error:
        raise RuntimeError(f"Gemini API request failed: {error}") from error

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError("Gemini API returned an unexpected response") from error


def extract_code(response):
    match = re.search(r"```(?:python)?\s*(.*?)```", response, flags=re.DOTALL | re.IGNORECASE)
    return (match.group(1) if match else response).strip() + "\n"


def validate_code(code):
    try:
        ast.parse(code)
    except SyntaxError as error:
        raise RuntimeError(f"Gemini returned invalid Python: {error}") from error


def dispatch_coding_task(prompt_instruction: str, output_file: Path | None = None):
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        print("Error: LLM_API_KEY environment variable is missing!")
        sys.exit(1)
        
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    timeout = float(os.getenv("GEMINI_TIMEOUT", "60"))
    print("Connecting to Gemini API...")
    if api_key == "test":
        generated_code = """# Local test response
def enterprise_feature_module():
    return True
"""
    else:
        generated_code = extract_code(request_gemini(prompt_instruction, api_key, model, timeout))
    validate_code(generated_code)

    target_file = output_file or Path(__file__).resolve().parent / "sandbox_agent_core.py"
    target_file.parent.mkdir(parents=True, exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(generated_code)
        
    print(f"Successfully dispatched and written response to {target_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="Create a secure enterprise telemetry module")
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    dispatch_coding_task(arguments.task, arguments.output)
