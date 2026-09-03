import time
import subprocess

def run_agent_pipeline():
    max_retries = 5
    attempt = 1

    while attempt <= max_retries:
        print(f"\n--- Memulai Siklus Agen Percobaan Ke-{attempt} ---")
        
        try:
            # 1. Jalankan generator untuk merakit/memperbarui kode
            print("Menjalankan generator...")
            subprocess.run(["python", "agent_generator.py"], check=True)

            # 2. Jalankan validator untuk uji sintaks
            print("Menjalankan validator...")
            subprocess.run(["python", "agent_validator.py"], check=True)

            # 3. Jalankan konektor LLM
            print("Menjalankan konektor agen...")
            subprocess.run(["python", "agent_connector.py"], check=True)

            print("✅ Siklus agen berhasil diselesaikan!")
            break # Berhenti dari loop jika sukses

        except subprocess.CalledProcessError as e:
            print(f"⚠️ Terdeteksi gangguan pada percobaan ke-{attempt}: {e}")
            print("Mencoba melakukan perbaikan otomatis dan uji coba ulang dalam 5 detik...")
            time.sleep(5)
            attempt += 1
        except Exception as ex:
            print(f"❌ Error tidak terduga: {ex}")
            break

if __name__ == "__main__":
    run_agent_pipeline()
