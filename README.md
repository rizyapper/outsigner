# outsigner
This project can be used to log out the users from every browser they logged in to. This makes their account secure when using a public computer.



# 🔐 Browser Session Cleaner 

> 🛡️ A simple tool to help users secure their browser sessions by removing sensitive login and session data — especially useful when using public or shared computers.

---

## 🧠 Overview

This Python-based script allows users to **clean browser session and login data** from common browsers like Chrome, Edge, and Firefox. 

It's ideal for situations where:
- You forget to **log out** from websites on a **public/shared computer**.
- You want to **clear saved credentials** and sessions without deleting entire browsing history.
- You need a quick manual cleanup tool before leaving a machine.

> 🔒 **This tool is currently designed for Windows operating systems**.

---

## ✅ Features

- Detects and processes browser profile directories.
- Deletes session and login-related files:
  - Cookies
  - Saved passwords
  - Web session data
- Supports:
  - **Google Chrome**
  - **Microsoft Edge**
  - **Mozilla Firefox**
- Simple, readable console output.

---

## 💡 How It Works

The script targets specific folders and files known to store session and login data.

### Chrome & Edge Targets:
- `Cookies`
- `Login Data`
- `Sessions`
- `Session Storage`
- `Web Data`
- `Network`

### Firefox Targets:
- `cookies.sqlite`
- `logins.json`
- `sessionstore.jsonlz4`

For each browser found on the system, the tool iterates through user profiles and removes the above data wherever it exists.

---

## 🖥️ Supported Browsers

| Browser        | Status      |
|----------------|-------------|
| Google Chrome  | ✅ Supported |
| Microsoft Edge | ✅ Supported |
| Mozilla Firefox| ✅ Supported |

---

## ⚙️ System Requirements

- OS: **Windows 10/11**
- Python: **3.x**
- No admin privileges required (but helps for full cleanup)

---

## 🚀 Usage

1. Download or clone this repository.
2. Run the script using Python:

```bash
python browser_cleaner.py
```

Disclaimer
This script is intended for personal use or for users with explicit permission on shared systems. It does not anonymize all data and does not replace proper logout hygiene. Use responsibly.
