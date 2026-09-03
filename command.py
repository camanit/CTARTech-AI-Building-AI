import argparse
from pathlib import Path


ROADMAP_FILE = Path("roadmap/ROADMAP.md")


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


def main():
    parser = argparse.ArgumentParser(description="CLI untuk menjalankan roadmap agent")
    parser.add_argument("command", choices=("init", "roadmap"))
    arguments = parser.parse_args()

    if arguments.command == "init":
        return initialize_project()
    return show_roadmap()


if __name__ == "__main__":
    raise SystemExit(main())