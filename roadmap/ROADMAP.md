# AI-Building-AI Roadmap

## Fase 1: Fondasi Agent

- [x] Membuat connector LLM awal
- [x] Membuat generator kode sandbox
- [x] Membuat validator kode Python
- [x] Membuat runner pipeline dengan retry
- [x] Membuat perintah CLI `init` dan `roadmap`

## Fase 2: Eksekusi Roadmap

- [x] Membaca semua task dari `ROADMAP.md`
- [x] Memilih task pertama yang belum selesai
- [x] Mengirim task ke connector LLM
- [ ] Menjalankan validator setelah kode dibuat
- [ ] Menjalankan test aplikasi di sandbox
- [ ] Mengubah status task menjadi `[x]` setelah berhasil

## Fase 3: Pengelolaan Project

- [x] Menambahkan perintah `python command.py run`
- [x] Menambahkan perintah `python command.py validate`
- [x] Menambahkan perintah `python command.py status`
- [ ] Menyimpan log setiap eksekusi agent
- [x] Membuat evaluator AI awal untuk menganalisis agent
- [ ] Menambahkan mekanisme persetujuan sebelum perubahan diterapkan

## Fase 4: Integrasi dan Keamanan

- [x] Menghubungkan connector ke provider LLM nyata
- [x] Menambahkan rotasi API key saat quota tercapai
- [ ] Menambahkan isolasi sandbox yang lebih kuat
- [ ] Menambahkan integrasi commit dan pull request GitHub
- [ ] Menambahkan pemeriksaan secret dan perubahan berisiko
