# 🚀 Spyder AI Coding Copilot (CLI Tool)

> 專為 Python 開發者設計的輕量化 Gemini AI 程式碼輔助工具，無需切換瀏覽器即可在 IDE Console 或命令列中即時生成程式碼。

---

## 📌 專案背景與簡介
在 Python 開發過程中，頻繁切換瀏覽器使用 AI 輔助容易中斷思緒。本專案透過 Google 官方 `google-genai` SDK，整合 `gemini-3.5-flash` 模型，打造一個能在命令列（CLI）或 Spyder Console 內即時互動的 AI 寫程式助手，並透過 PyInstaller 打包成獨立 `.exe` 執行檔。

## 🌟 核心特色
- **IDE 無縫寫作**：直接在 Console 輸入需求，即時獲得附帶關鍵註解的 Python 範例。
- **動態 API Key 管理**：支援自動讀取系統環境變數 `GEMINI_API_KEY`，亦提供互動式手動輸入，避免金鑰硬編碼外洩。
- **自動重試機制 (Robustness)**：針對 API 流量高峰期的 `503 Service Unavailable` 錯誤建立自動重試邏輯。
- **零環境依賴**：打包為獨立 `.exe` 檔案，使用者電腦無需安裝 Python 環境即可運行。

## 📦 安裝與使用說明

### 方式 A：直接下載 `.exe` 執行檔（推薦）
1. 至本專案的 [Releases](../../releases) 頁面下載最新版 `打包程式輔助_AI.exe`。
2. 雙擊執行檔案，依照提示輸入您的 Gemini API Key。
3. 輸入程式碼開發需求（輸入 `exit` 或 `quit` 即可結束對話）。

### 方式 B：從原始碼運行
```bash
# 1. 複製專案
git clone [https://github.com/你的帳號/spyder-gemini-assistant.git](https://github.com/你的帳號/spyder-gemini-assistant.git)
cd spyder-gemini-assistant

# 2. 安裝依賴套件
pip install google-genai

# 3. 執行程式
python spyder_ai_copilot.py

# 🚀 Spyder AI Copilot (CLI Tool)

A lightweight, high-performance Command Line Interface (CLI) AI assistant powered by the official **Google Gemini API** (`google-genai` SDK). Designed to provide instant Python code generation, debugging assistance, and query responses directly inside your terminal or Spyder IDE environment.

---

## ✨ Features

- **Instant Startup Optimizations**: Utilizes lazy imports to eliminate console boot latency.
- **Robust Error Handling**:
  - Auto-retry with backoff mechanism for `503 Service Unavailable` errors.
  - User-friendly CLI alerts for `429 RESOURCE_EXHAUSTED` (API Free-Tier Rate Limits).
- **Flexible Authentication**: Automatically detects `GEMINI_API_KEY` from system environment variables or local `*_key.txt` files, with fallback to interactive prompt input.
- **Developer-Centric Persona**: Pre-configured system instructions tailored specifically for clean, production-ready Python code snippets.

---

## 🚀 Quick Start (Executable)

No Python environment required!

1. Go to the [Releases](https://github.com/weijj24-cmd/spyder_ai_copilot/releases) section on the right sidebar.
2. Download the latest `spyder_ai_copilot.exe` (or `.zip` release).
3. Run the executable and enter your Gemini API Key when prompted.

---

## 🛠️ Running from Source

### Prerequisites
- Python 3.10+
- Google Gemini API Key ([Get one here](https://aistudio.google.com/))

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/weijj24-cmd/spyder_ai_copilot.git](https://github.com/weijj24-cmd/spyder_ai_copilot.git)
   cd spyder_ai_copilot
