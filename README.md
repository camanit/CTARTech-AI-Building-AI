# CTARTech AI-Building-AI
Experimental workspace and meta-framework for self-improving AI coding agents and automated repository generation.

## Overview
Prototype open source untuk membangun dan mengevaluasi coding agent berbasis LLM. Agent membaca roadmap, meminta kode dari Gemini, memvalidasi hasilnya, lalu menyimpannya ke folder `app/`.

## Struktur Project

```text
AI-Building-AI/
├── agent/                 # Komponen agent dan connector Gemini
├── app/                   # Kode aplikasi hasil eksekusi agent
├── roadmap/ROADMAP.md     # Task dan status pekerjaan
├── command.py             # CLI utama
└── README.md
```

## Cara Kerja AI dan Roadmap

AI bekerja dengan membaca perintah dan roadmap, lalu mengerjakan pekerjaan secara bertahap. Setiap task idealnya melewati alur berikut:

```text
Roadmap -> pilih task berikutnya -> generate kode -> validasi -> jalankan sandbox -> update status
```

Roadmap yang detail membuat pekerjaan AI lebih terarah. Task sebaiknya ditulis kecil, berurutan, dan memiliki hasil yang dapat diuji.

### Perintah CLI

Inisialisasi project dan masukkan pekerjaan yang ingin dibuat:

```bash
python command.py init
```

Contoh input untuk repository ini:

```text
Membangun AI-Building-AI agar dapat mengeksekusi roadmap secara otomatis
```

Perintah tersebut membuat folder `app/`, `tests/`, `agent/`, dan `roadmap/`, lalu menyimpan task awal ke `roadmap/ROADMAP.md`.

Untuk melihat roadmap:

```bash
python command.py roadmap
```

Perintah `init`, `roadmap`, `run`, `validate`, `evaluate`, dan `status` sudah tersedia.

Untuk mengevaluasi struktur agent dan membuat proposal perbaikan:

```bash
python command.py evaluate
```

Evaluator menulis `app/evaluation_report.md` dan `app/improvement_proposal.md`. Evaluator hanya menganalisis file dan membuat proposal; ia tidak mengubah folder `agent/` secara otomatis.

### Contoh Roadmap

```markdown
# AI-Building-AI Roadmap

## Fase 1: Fondasi Agent

- [x] Membuat connector LLM
- [x] Membuat validator kode
- [x] Membuat pipeline dengan retry

## Fase 2: Eksekusi Roadmap

- [ ] Membaca task berikutnya
- [ ] Membuat kode di `app/`
- [ ] Menjalankan test
- [ ] Memperbarui status task
```

Pada eksekusi roadmap, AI mengambil task pertama yang belum selesai, membuat perubahan kode, menjalankan validator, kemudian mengubah status task menjadi `[x]` hanya jika pemeriksaan berhasil. Jika terjadi error, status task tidak diubah dan error dilaporkan untuk ditinjau.

### Pipeline Agent

Pipeline dasar saat ini dapat dijalankan dengan:

```bash
python agent/runner_loop.py
python command.py run
```

Pipeline menjalankan connector, memvalidasi hasil kode, lalu mengeksekusi sandbox. `command.py` menjadi pintu masuk utama dan meneruskan perintah ke pipeline di folder `agent/`.

### Konfigurasi Gemini

Connector sudah menyediakan pemanggilan Gemini API. Pengguna cukup mengatur API key di environment:

```bash
export LLM_API_KEY="GEMINI_API_KEY_ANDA"
export GEMINI_MODEL="gemini-2.5-flash"
python command.py run
```

`GEMINI_MODEL` dan `GEMINI_TIMEOUT` bersifat opsional. Default model adalah `gemini-2.5-flash` dan default timeout adalah 60 detik. API key tidak boleh ditulis di source code atau di-commit ke GitHub.

Untuk menggunakan beberapa API key dan berpindah otomatis ketika quota atau rate limit tercapai:

```bash
export LLM_API_KEYS="GEMINI_KEY_1,GEMINI_KEY_2,GEMINI_KEY_3"
python command.py run
```

Connector mencoba key secara berurutan. `LLM_API_KEYS` diprioritaskan jika tersedia; jika tidak, connector menggunakan `LLM_API_KEY`. Nilai key tidak pernah dicetak ke log.

### Status Prototype

Yang sudah berjalan otomatis:

- `command.py run` membaca task pertama dengan status `[ ]`.
- Connector mengirim task ke Gemini dan mem-parsing kode hasilnya.
- Kode divalidasi sebelum ditulis ke `app/`.
- Task berubah menjadi `[x]` setelah validasi berhasil.
- `command.py evaluate` membuat report dan proposal perbaikan.

Yang belum berjalan otomatis:

- Test aplikasi belum dijalankan oleh executor.
- Satu kali `run` baru mengerjakan satu task.
- Agent belum mengubah dirinya sendiri tanpa approval.
- Commit, pull request, rollback, dan sandbox terisolasi belum tersedia.

Dengan demikian, sistem ini adalah executor roadmap prototype dengan connector Gemini. Pengembangan self-improvement tetap menggunakan evaluasi, review manusia, test, dan rollback.

Jangan commit API key, file `.env`, atau secret apa pun ke repository.
