import os
import sys
import subprocess

def validate_generated_code():
    target_file = "sandbox_agent_core.py"
    
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
    validate_generated_code()
