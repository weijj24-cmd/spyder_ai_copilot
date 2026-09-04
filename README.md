# 🚀 Spyder AI Coding Copilot (CLI Tool)

### 專為 Python 開發者設計的輕量化 Gemini AI 程式碼輔助工具，無需切換瀏覽器即可在 IDE Console 或命令列中即時生成程式碼。
### A lightweight, terminal-based Gemini AI coding assistant designed for Python developers. Generate, debug, and refactor code directly inside your IDE Console or CLI without context-switching to a browser.

---

## 📌 專案背景與簡介 / Project Overview

**[中文]**
在 Python 開發過程中，頻繁切換瀏覽器使用 AI 輔助容易中斷思緒。本專案透過 Google 官方 `google-genai` SDK，整合 `gemini-3.5-flash` 模型，打造一個能在命令列（CLI）或 Spyder Console 內即時互動的 AI 寫程式助手，並透過 PyInstaller 打包成獨立 `.exe` 執行檔。

**[English]**
Frequent context-switching between code editors and web browsers degrades developer focus and productivity. **Spyder AI Coding Copilot** leverages Google's official `google-genai` SDK and the high-performance `gemini-3.5-flash` model to deliver seamless, terminal-native AI assistance. Packaged with PyInstaller into a standalone executable, it allows developers to query, generate, and optimize Python code instantly within Spyder Console, CMD, or PowerShell.

---

## 🌟 核心特色 / Key Features

- **IDE 無縫寫作 (Seamless IDE Workflow)**：直接在 Console 輸入需求，即時獲得附帶關鍵註解的 Python 範例程式碼。
- **動態 API Key 管理 (Dynamic API Key Management)**：支援自動讀取系統環境變數 `GEMINI_API_KEY` 或本地 `*_key.txt` 檔案，亦提供互動式手動輸入，避免金鑰硬編碼外洩。
- **延遲載入優化 (Lazy Module Loading)**：採用延遲匯入技術，解決 PyInstaller 打包後啟動時的黑畫面等待問題，實現毫秒級顯示歡迎介面。
- **自動重試機制 (Robust Fault Tolerance)**：建立自動重試機制，針對 API 流量高峰期的 `503 Service Unavailable` 自動重試，並對 `429 RESOURCE_EXHAUSTED` 頻率限制提供友善提示。
- **零環境依賴 (Zero-Dependency Distribution)**：打包為獨立 `.exe` 執行檔與目錄包，使用者電腦無需安裝 Python 環境即可立即運行。

---

## 📦 安裝與使用說明 / Installation & Quick Start

### 方式 A：直接下載執行檔 / Method A: Standalone Executable (Recommended)
1. 至本專案的 [Releases](https://github.com/weijj24-cmd/spyder_ai_copilot/releases) 頁面下載最新版 `.exe` 執行檔或壓縮包。
   Download the latest `spyder_ai_copilot.exe` (or release package) from the Releases page.
2. 雙擊執行檔案，依照提示輸入您的 Gemini API Key。
   Launch the executable and enter your Google Gemini API Key when prompted.
3. 輸入程式碼開發需求（輸入 `exit` 或 `quit` 即可結束對話）。
   Type your development prompt. Type `exit` or `quit` to terminate the session.

### 方式 B：從原始碼運行 / Method B: Run from Source

```bash
# 1. 克隆專案 / Clone the repository
git clone [https://github.com/weijj24-cmd/spyder_ai_copilot.git](https://github.com/weijj24-cmd/spyder_ai_copilot.git)
cd spyder_ai_copilot

# 2. 安裝依賴套件 / Install dependencies
pip install google-genai

# 3. 設定 API 金鑰 (選填) / Configure API Key (Optional)
set GEMINI_API_KEY=your_gemini_api_key_here

# 4. 執行程式 / Execute the copilot
python spyder_ai_copilot.py
