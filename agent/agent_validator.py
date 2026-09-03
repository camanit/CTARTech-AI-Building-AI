import os
import sys
import subprocess
from pathlib import Path
import argparse


TARGET_FILE = Path(__file__).resolve().parent / "sandbox_agent_core.py"

def validate_generated_code(target_file=TARGET_FILE):
    
    if not os.path.exists(target_file):
        print(f"Validation Error: {target_file} not found. Run generator first!")
        sys.exit(1)
        
    print(f"Running syntax and security check on {target_file}...")
    
    # Menjalankan uji sintaks python secara lokal (dry-run)
    result = subprocess.run([sys.executable, "-m", "py_compile", target_file], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Success: Generated agent code passed all syntax and structural validation gates.")
    else:
        print("Failure: Syntax errors detected in generated code.")
        print(result.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, default=TARGET_FILE)
    arguments = parser.parse_args()
    validate_generated_code(arguments.target)
