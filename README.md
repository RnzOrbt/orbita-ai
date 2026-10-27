# Orbita_Ai

Your own AI chat that runs **only on your own laptop** using linux mint operating system. Nothing is sent to a company's server. It costs nothing and has no limits.

Open it on the laptop, or on any phone or computer using the same Wi-Fi.

## What it can do

- Answer questions in a chat page
- Talk back to you out loud (Voice on / off)
- Listen to you with the Mic button (use Chrome or Safari)
- Tell you the live weather for any city
- Switch between fast answers (Low) and deep answers (Max)

## The laptop it runs on

This was built and tested on a small, old laptop. If your laptop is similar or better, it will work.

| Part | What it is |
|---|---|
| Laptop | Acer Aspire A314-21 (made around 2019) |
| Brain (CPU) | AMD A6-9220e, 2 cores, 1.2 to 1.6 GHz |
| Memory (RAM) | 4 GB (about 3.7 GB usable) |
| Extra memory (swap) | 4 GB, uses the hard drive |
| Storage | 500 GB hard drive (WD5000LPCX, a spinning disk, not an SSD) |
| Graphics | AMD Radeon R4, built into the CPU (not used by the AI) |
| Screen | 1366 x 768 |
| Wi-Fi | Qualcomm Atheros QCA9377 (802.11ac) |
| Cable internet | Realtek Gigabit Ethernet |
| Bluetooth | Version 4.2 |
| Battery | 37 Wh |
| Operating system | Linux Mint 22.3 "Zena" (based on Ubuntu 24.04) |
| Desktop | Cinnamon 6.6.9 |

Your CPU must support **AVX** (the voice needs it). This laptop does.

### Minimum specs you need (for other pc)

- Any 64-bit laptop or PC running Linux (Linux Mint or Ubuntu is easiest)
- 4 GB of RAM or more
- About 5 GB of free disk space
- Internet for the one-time setup downloads
- A CPU with AVX (check with `lscpu | grep -o -w avx`)

### What to expect on this laptop

It works, but it is **slow**. A short answer takes a few seconds. A long answer can take a minute or more. Tips: use Low or Medium effort, and turn Voice off for faster answers.

## What is in this folder

| File | What it is |
|---|---|
| `index.html` | The chat page you see in the browser |
| `docs/SETUP.pdf` | Step-by-step setup guide. Start here. |
| `deploy/orbita.conf` | Setting for nginx, the program that opens the page |
| `deploy/laptop-ai.service` | Makes the AI start by itself when the laptop turns on |
| `deploy/piper-voice.service` | Makes the voice start by itself |
| `deploy/voice_server.py` | Small program that turns text into speech |
| `.gitignore` | Stops big or private files from being uploaded by mistake |
| `sysflow/orbita-ai-sysflow.gif` | Visual presentation of how things work on this project |

The AI model and voice files are big, so they are **not** in this folder. The guide shows where to download them.

## How to set it up

Open `docs/SETUP.pdf` and follow it from the top. It uses simple copy-and-paste steps.

In the `deploy` files, change `YOUR_USER` to your own Linux username. To find it, type `whoami` in the Terminal.

## A reminder

- Use it at home only. On plain Wi-Fi, anyone on your Wi-Fi can use it.
- Do not open any port on your router.
- To use it away from home, install Tailscale. It keeps strangers out.
- Never put a password or key inside `index.html`. Everyone who opens the page can see that file.
- Never upload the model files, passwords, or `.htpasswd`.
