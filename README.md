# ⌖ Port.Scan

**A self-hosted network port scanner — Flask backend, Python scanning core, zero cloud dependency.**

[![License: MIT](https://img.shields.io/badge/License-MIT-00d4ff.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-00d4ff.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-00d4ff.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/status-active-2dff8a.svg)](#)

[Features](#-features) • [Screenshots](#-screenshots) • [Getting Started](#-getting-started) • [Usage](#-usage) • [Project Structure](#-project-structure) • [License](#-license)

</div>

---

## Overview

Port.Scan is a lightweight, self-hosted port scanner you run on your own machine. No accounts, no telemetry, no data leaving your network — a Flask app drives a small Python scanning core, and the results render straight in your browser.

Built as a personal / learning project, not an enterprise product — it's meant to be cloned, read, and modified.

> ⚠️ **Only scan hosts and networks you own or are explicitly authorized to test.** Scanning systems without permission may be illegal in your jurisdiction.

---

## ✦ Features

- **TCP, UDP, and Full scan modes** — with honest UDP results (no false "everything is open" reports; ambiguous no-response ports are reported separately, not guessed at)
- **Known-service detection** — recognized ports (SSH, HTTP, MySQL, RDP, etc.) are labeled automatically
- **Inline results** — see what a scan found immediately, no page reload required
- **Persistent scan history** — every scan is saved locally to SQLite and shown in a running log
- **Threaded scanning** — concurrent port checks instead of a slow sequential loop
- **Fully self-hosted** — your data never leaves your machine

---

## 🖼 Screenshots

<!-- 
  Add your screenshots to docs/screenshots/ and update the paths below.
  Recommended: PNG, ~1200px wide, dark-mode browser chrome to match the UI.
-->

<div align="center">

### Home — Scanner

![Home screen showing the scanner form](docs/screenshots/home.png)

### Scan Results

![Inline scan results with known/unrecognized/no-response port groups](docs/screenshots/scan-results.png)

### Scan History

![Recent scans table](docs/screenshots/scan-history.png)

### Docs Page

![Documentation page](docs/screenshots/docs-page.png)

</div>

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/swe74-29/Python-FlaskWeb-PortScanner.git
cd Python-FlaskWeb-PortScanner

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## 🕹 Usage

1. Enter a **target host** — an IP address or hostname (e.g. `192.168.1.1` or `example.com`)
2. Set a **port range** — from `1` to `65535`
3. Choose a **scan mode**:

   | Mode | Description |
   |------|-------------|
   | `TCP` | Standard TCP connect scan — fast and reliable |
   | `UDP` | UDP probe scan — slower, results can be ambiguous by nature of the protocol |
   | `Full` | Runs both TCP and UDP across the given range |

4. Click **Initiate Scan** — results appear inline, grouped into:
   - **Known services** — recognized ports with a labeled service name
   - **Unrecognized** — open ports with no known service match
   - **No response** *(UDP only)* — ports that neither confirmed open nor closed; a real limitation of UDP, not a bug

Every completed scan is also logged to the **Recent Scans** table for later reference.

---

## 📁 Project Structure

```
Python-FlaskWeb-PortScanner/
├── app.py                  # Flask entry point + routes
├── scanner.py               # TCP/UDP scanning logic + service classification
├── requirements.txt
├── LICENSE
├── README.md
├── static/
│   ├── style.css            # Shared styling for docs/about/github/license/source pages
│   └── favicon.svg
├── templates/
│   ├── index.html           # Scanner + results + history
│   ├── docs.html
│   ├── about.html
│   ├── github.html
│   ├── license.html
│   └── source.html
└── docs/
    └── screenshots/          # Screenshots referenced in this README
```

---

## 🔌 Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Scanner form + scan history |
| `/scan` | POST | Runs a scan, renders results inline |
| `/docs` | GET | Documentation |
| `/about` | GET | About the project |
| `/github` | GET | Repository info |
| `/license` | GET | MIT license (rendered) |
| `/source` | GET | Source layout + contribution notes |

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo and create a branch off `main`
2. Keep pull requests focused — one change per PR
3. Open an [issue](https://github.com/swe74-29/Python-FlaskWeb-PortScanner/issues) first for anything larger than a small fix

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for the full text.

Copyright © 2026 Sweta Halder

---

## 👤 Author

**Sweta Halder**

- GitHub: [@swe74-29](https://github.com/swe74-29)
- Email: [swetahalder29@gmail.com](mailto:swetahalder29@gmail.com)

---

<div align="center">
<sub>Built with Flask &amp; Python</sub>
</div>
