import subprocess
import sys

def run_agent_pipeline():
    max_retries = 5

    for attempt in range(1, max_retries + 1):
        print(f"\n--- Memulai Siklus Agen Percobaan Ke-{attempt} ---")
        
        try:
            print("Menjalankan konektor agen...")
            subprocess.run([sys.executable, "agent_connector.py"], check=True)

            print("Menjalankan validator...")
            subprocess.run([sys.executable, "agent_validator.py"], check=True)

            print("Menjalankan sandbox...")
            subprocess.run([sys.executable, "sandbox_agent_core.py"], check=True)

            print("✅ Siklus agen berhasil diselesaikan!")
            return True

        except subprocess.CalledProcessError as e:
            print(f"⚠️ Terdeteksi gangguan pada percobaan ke-{attempt}: {e}")
            if attempt < max_retries:
                print("Mencoba ulang...")
        except Exception as ex:
            print(f"❌ Error tidak terduga: {ex}")
            return False

    return False

if __name__ == "__main__":
    run_agent_pipeline()
