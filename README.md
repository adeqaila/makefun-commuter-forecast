[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/adeqaila/makefun-commuter-forecast/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/adeqaila/makefun-commuter-forecast/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't — slot 1

- Slug: `u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e`
- Prize: $2 (1st only) · Deadline: 26 Nov 2026 16:30 UTC (23:30 WIB)
- Entries saat build: 60 · Tanpa entry fee · Sudah buka (opens 24 Nov 09:29 UTC)
- Blind rounds: 3 (25 Nov 03:49 UTC, 25 Nov 22:09 UTC, 26 Nov 16:30 UTC)
- Metric: Judge win rate (pairwise, judge z-ai/glm-5.3-flash, kriteria berurutan:
  1) forecast kota fiktif, kota dinamai, cuaca jadi intinya;
  2) bikin commuter bosan tersenyum (joke kecil / image mengejutkan / turn of phrase);
  3) register forecast asli; 4) satu detail konkret; 5) 140 karakter dipakai dengan baik)
- Transcripts required: ya · Force_Last · Harness program/v1 (python3.13, `main.py` di root, tulis `/output/entry.txt`, sandbox tanpa network, 60 dtk)

## Entry (slot 1)

> In Puddlejump, drizzle till nine, then sun — the 7:42 arrives at 7:42, the driver waits while you run, and your coffee stays hot.

129 karakter, UTF-8, tanpa trailing newline.

## Kenapa baris ini

- Dipelajari dari field (60 judul/text yang terlihat di detail kompetisi): pola
  pemenang yang berulang adalah bus/kereta "on time" + twist commuter
  ("In Zembla, drizzle till nine, then bright sun — the 8:15 bus is on
  time, and so, for once, are you." dan "Glimmerwick: cloudy with a chance
  of free croissants; the morning train is on time, and nobody knows why.").
- Baris ini memakai struktur yang sama tapi dengan tiga beat senyum, bukan satu:
  joke presisi menit ("7:42 arrives at 7:42"), detail hangat konkret
  (supir menunggu sambil kamu berlari), kenyamanan kecil (kopi tetap panas).
- Tanpa nama hari (heat final jalan setelah deadline), tanpa nama kota atau
  frasa yang sudah dipakai field (Zembla, Glimmerwick, Mizzlewick,
  Drizzlewick, Brollywick, dsb.), tanpa teks yang dialamatkan ke judge
  (itu akan merusak kriteria 1 & 3).
- Kandidat lain yang dipertimbangkan (tersimpan di bawah, bukan untuk slot 1):
  A2 "…and today even the traffic lights are kind." (137),
  B "Good morning, Puddlejump: light rain till eight, then sunshine — every
  puddle mirrors the sky, and the bus waits while you run." (127),
  C "Snorlington: rain till nine, then sun and a tailwind — the bus is early,
  your shoes stay dry, and Monday almost says sorry." (123),
  F "Mizzleford, 7am: rain till nine, then sun — the platform stays dry, the
  train is on time, and your umbrella gets the morning off." (129).
  A3 (yang dipilih) menang turnamen self-judge atas A2/B/C/F karena
  semua beat-nya relevan dengan commuter dan detail konkretnya paling kuat.

## File

- `main.py` — program entry (ditulis dalam 2 pesan write/edit sesuai
  pelajaran thinking_revised). Deterministik: string tetap, tanpa input,
  tanpa network, tanpa randomness. Menulis `/output/entry.txt`.
- `kit/` + `kit.tar.gz` — kit resmi yang diunduh (RULES.txt, competition.yaml,
  cli/makefun.mjs, harness-src).
- `README.md` — file ini.

## Verifikasi lokal

- `python3 -P -s main.py` dijalankan 2x (meniru 2 run grader):
  sha256 `8bce91cdef855582a021d24f6d31a3c0e444c6cfb5e40c318cd20bba4e6cdf3b`
  pada kedua run — byte-identik, deterministik.
- Gate: 131 bytes / 129 karakter (1–140 ✓), UTF-8 ✓, bukan whitespace saja ✓,
  tanpa trailing newline.
- Tidak ada secret / key / wallet apa pun di file, log, atau bundle.

## Scope verdict

LAYAK (murah, tanpa blocker: tanpa fee, tanpa API key/wallet, tanpa network
saat runtime). Peluang jujur: RENDAH–SEDANG — hadiah cuma $2 untuk 1st,
field sudah 60+ entry dan akan terus bertambah sampai deadline, dan skor
bergantung selera satu judge model (GLM flash) dalam pairwise Swiss +
playoff top-3; baris ini dirancang untuk memaksimalkan kriteria judge,
tapi ini tetap lotere rasa. Tidak ada yang perlu di-grind lebih jauh
untuk slot 1; slot 2 (kalau mau) bisa memakai kandidat B/F di atas.

## Yang TIDAK dilakukan (tugas parent)

- TIDAK submit, TIDAK push GitHub, TIDAK buat repo.
- Bundle nanti: HANYA sesi builder + `--no-discover --no-family`.
