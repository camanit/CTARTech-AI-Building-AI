import os
import sys
import argparse
from pathlib import Path


def dispatch_coding_task(prompt_instruction: str, output_file: Path | None = None):
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        print("Error: LLM_API_KEY environment variable is missing!")
        sys.exit(1)
        
    print("Connecting to LLM Provider gateway...")
    # Logika pengiriman prompt ke API LLM
    # Contoh struktur payload yang mematuhi AGENT_CODING_RULES.md
    
    generated_code = f"""# Auto-generated via LLM Connector
# Task: {prompt_instruction}

def enterprise_feature_module():
    print("Executing secure routine based on enterprise specifications.")
    return True
"""
    
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
