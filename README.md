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

Contoh input:

```text
Membuat aplikasi klinik dengan modul pasien dan dokter
```

Perintah tersebut membuat folder `app/`, `tests/`, `agent/`, dan `roadmap/`, lalu menyimpan task awal ke `roadmap/ROADMAP.md`.

Untuk melihat roadmap:

```bash
python command.py roadmap
```

Perintah `init` dan `roadmap` sudah tersedia. Perintah `run`, `validate`, dan `status` merupakan bagian dari pengembangan CLI berikutnya.

### Contoh Roadmap Aplikasi Klinik

```markdown
# Roadmap Aplikasi Klinik

- [ ] Buat model data pasien
- [ ] Buat API pasien
- [ ] Buat halaman daftar pasien
- [ ] Tambahkan test pasien
- [ ] Buat model data dokter
- [ ] Buat modul jadwal pemeriksaan
```

Pada eksekusi roadmap penuh, AI akan mengambil task pertama yang belum selesai, membuat perubahan kode, menjalankan validator dan test, kemudian mengubah status task menjadi `[x]` hanya jika pemeriksaan berhasil. Jika terjadi error, proses berhenti atau mencoba ulang sesuai konfigurasi dan melaporkan error untuk ditinjau.

### Pipeline Agent

Pipeline saat ini dapat dijalankan dengan:

```bash
python runner_loop.py
```

Pipeline menjalankan connector, memvalidasi hasil kode, lalu mengeksekusi sandbox. Connector saat ini masih berupa simulasi lokal; integrasi provider LLM memerlukan `LLM_API_KEY` dan implementasi request ke provider yang dipilih.
