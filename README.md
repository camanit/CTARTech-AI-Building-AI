# CTARTech AI-Building-AI
Experimental workspace and meta-framework for self-improving AI coding agents and automated repository generation.

## Overview
This repository serves as a secure, isolated sandbox to design, test, and validate multi-provider LLM coding agents, workflow pipelines, and automated patch architectures before deploying them to production systems.

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

Perintah `init`, `roadmap`, `run`, `validate`, dan `status` sudah tersedia.

### Contoh Roadmap AI-Building-AI

```markdown
# AI-Building-AI Roadmap

## Fase 1: Fondasi Agent

- [x] Membuat connector LLM awal
- [x] Membuat generator kode sandbox
- [x] Membuat validator kode Python
- [x] Membuat runner pipeline dengan retry

## Fase 2: Eksekusi Roadmap

- [ ] Membaca task roadmap
- [ ] Menjalankan task berikutnya
- [ ] Memvalidasi hasil kode
- [ ] Memperbarui status task
```

Pada eksekusi roadmap penuh, AI akan mengambil task pertama yang belum selesai, membuat perubahan kode, menjalankan validator dan test, kemudian mengubah status task menjadi `[x]` hanya jika pemeriksaan berhasil. Jika terjadi error, proses berhenti atau mencoba ulang sesuai konfigurasi dan melaporkan error untuk ditinjau.

### Pipeline Agent

Pipeline dasar saat ini dapat dijalankan dengan:

```bash
python agent/runner_loop.py
python command.py run
```

Pipeline menjalankan connector, memvalidasi hasil kode, lalu mengeksekusi sandbox. `command.py` menjadi pintu masuk utama dan meneruskan perintah ke pipeline di folder `agent/`.

### Status Otomatisasi Saat Ini

Yang sudah berjalan otomatis:

- `runner_loop.py` menjalankan connector, validator, dan sandbox secara berurutan.
- Runner memiliki mekanisme retry jika salah satu proses gagal.
- `command.py` menyediakan perintah `run`, `validate`, dan `status`.

Yang belum berjalan otomatis:

- `agent_generator.py` belum dipanggil oleh runner.
- Roadmap belum dibaca untuk memilih task berikutnya.
- Kode hasil agent belum diarahkan untuk membangun fitur di folder `app/`.
- Status task roadmap belum diubah otomatis dari `[ ]` menjadi `[x]`.
- Connector masih berupa simulasi lokal, bukan request ke provider LLM nyata.

Dengan demikian, sistem saat ini adalah pipeline agent dasar yang sudah dapat dieksekusi, bukan executor roadmap penuh. Tahap berikutnya adalah menghubungkan pembacaan roadmap, pembuatan kode di `app/`, pengujian, dan pembaruan status task.
