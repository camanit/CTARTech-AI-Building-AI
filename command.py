import argparse
import re
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
ROADMAP_FILE = PROJECT_ROOT / "roadmap/ROADMAP.md"
AGENT_DIR = PROJECT_ROOT / "agent"


def initialize_project():
    task = input("Masukkan yang mau dieksekusi: ").strip()
    if not task:
        print("Task tidak boleh kosong.")
        return 1

    for directory in ("app", "tests", "agent", "roadmap"):
        Path(directory).mkdir(exist_ok=True)

    ROADMAP_FILE.write_text(
        "# Project Roadmap\n\n"
        f"- [ ] {task}\n",
        encoding="utf-8",
    )
    print(f"Roadmap dibuat: {ROADMAP_FILE}")
    print(f"Task pertama: {task}")
    return 0


def show_roadmap():
    if not ROADMAP_FILE.exists():
        print("Roadmap belum ada. Jalankan: python command.py init")
        return 1

    print(ROADMAP_FILE.read_text(encoding="utf-8"), end="")
    return 0


def get_next_task():
    if not ROADMAP_FILE.exists():
        return None

    for line in ROADMAP_FILE.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^- \[ \] (.+)$", line)
        if match:
            return match.group(1)
    return None


def mark_task_completed(task):
    roadmap = ROADMAP_FILE.read_text(encoding="utf-8")
    pending_line = f"- [ ] {task}"
    completed_line = f"- [x] {task}"
    if pending_line not in roadmap:
        return False

    ROADMAP_FILE.write_text(roadmap.replace(pending_line, completed_line, 1), encoding="utf-8")
    return True


def execute_roadmap():
    task = get_next_task()
    if task is None:
        print("Tidak ada task roadmap yang masih terbuka.")
        return 0

    output_file = PROJECT_ROOT / "app" / "generated_feature.py"
    connector_file = AGENT_DIR / "agent_connector.py"
    validator_file = AGENT_DIR / "agent_validator.py"
    print(f"Menjalankan task: {task}")

    try:
        subprocess.run(
            [sys.executable, str(connector_file), "--task", task, "--output", str(output_file)],
            cwd=PROJECT_ROOT,
            check=True,
        )
        subprocess.run(
            [sys.executable, str(validator_file), "--target", str(output_file)],
            cwd=PROJECT_ROOT,
            check=True,
        )
    except subprocess.CalledProcessError:
        print("Task gagal. Status roadmap tidak diubah.")
        return 1

    if mark_task_completed(task):
        print(f"Task selesai: {task}")
        return 0
    print("Task tervalidasi, tetapi status roadmap gagal diperbarui.")
    return 1


def run_agent():
    runner_file = AGENT_DIR / "runner_loop.py"
    return subprocess.run([sys.executable, str(runner_file)], cwd=PROJECT_ROOT).returncode


def validate_agent():
    validator_file = AGENT_DIR / "agent_validator.py"
    return subprocess.run([sys.executable, str(validator_file)], cwd=PROJECT_ROOT).returncode


def show_status():
    if not ROADMAP_FILE.exists():
        print("Roadmap belum ada. Jalankan: python command.py init")
        return 1

    roadmap = ROADMAP_FILE.read_text(encoding="utf-8")
    completed = len(re.findall(r"^- \[x\] ", roadmap, flags=re.MULTILINE))
    remaining = len(re.findall(r"^- \[ \] ", roadmap, flags=re.MULTILINE))
    print(f"Selesai: {completed}")
    print(f"Belum selesai: {remaining}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="CLI untuk menjalankan roadmap agent")
    parser.add_argument(
        "command",
        choices=("init", "roadmap", "run", "validate", "status"),
    )
    arguments = parser.parse_args()

    if arguments.command == "init":
        return initialize_project()
    if arguments.command == "roadmap":
        return show_roadmap()
    if arguments.command == "run":
        return execute_roadmap()
    if arguments.command == "validate":
        return validate_agent()
    return show_status()


if __name__ == "__main__":
    raise SystemExit(main())