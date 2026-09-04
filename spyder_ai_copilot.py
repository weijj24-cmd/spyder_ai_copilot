import sys
import time

# 先印出歡迎畫面與提示，讓使用者即時看到回應
print("==========================================")
print("🚀 Gemini AI 程式開發助手 (CLI 工具)")
print("==========================================")
print("⏳ 正在載入系統模組與 API 設定，請稍候...\n")

# --------------------------------------------------
# 延遲匯入龐大套件（放這裏能避免點開 EXE 時產生長達數秒的黑畫面）
# --------------------------------------------------
try:
    import os
    from google import genai
except ImportError:
    print("❌ 錯誤：未安裝 google-genai 套件。請先執行 pip install google-genai")
    sys.exit(1)


def get_api_key():
    """取得 API Key：優先讀取環境變數，若無則要求使用者手動輸入"""
    api_key = os.environ.get("GEMINI_API_KEY")

    # 如果沒有環境變數，尋找本地 txt 金鑰檔
    if not api_key:
        key_files = [f for f in os.listdir(".") if f.endswith("_key.txt")]
        if key_files:
            try:
                with open(key_files[0], "r", encoding="utf-8") as f:
                    api_key = f.read().strip()
                print(f"🔑 已自動讀取金鑰檔案：{key_files[0]}")
            except Exception:
                pass

    # 若依然沒有金鑰，則提示手動輸入
    if not api_key:
        print("⚠️ 未檢測到 GEMINI_API_KEY 環境變數或金鑰檔案。")
        api_key = input("🔑 請輸入您的 Gemini API Key: ").strip()
        while not api_key:
            api_key = input("❌ 金鑰不能為空，請重新輸入: ").strip()

    return api_key


def ask_gemini(client, prompt: str):
    """發送 Prompt 至 Gemini 並處理自動重試機制"""
    print("\n🤖 Gemini 思考中...\n")
    sys_instruction = "你是一個專業的 Python 程式輔助 AI。請針對使用者的需求，優先提供精簡、正確且附帶關鍵註解的 Python 程式碼。"

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
                config={"system_instruction": sys_instruction},
            )
            print("====== 生成結果 ======\n")
            print(response.text)
            print("\n" + "=" * 22 + "\n")
            return
        except Exception as e:
            if "503" in str(e) and attempt < max_retries - 1:
                print(f"⚠️ 伺服器忙碌中 (503)，正在進行第 {attempt + 1} 次自動重試...")
                time.sleep(2)
            else:
                print(f"❌ 發生錯誤：{e}\n")
                break


def main():
    api_key = get_api_key()

    try:
        # 初始化 GenAI Client
        client = genai.Client(api_key=api_key)
        print("✅ 系統模組載入完成！Ready.\n")
    except Exception as e:
        print(f"❌ API Client 初始化失敗：{e}")
        return

    print("輸入你的需求（例如：『幫我用 pandas 讀取 csv』）")
    print("🚪 輸入 'exit' 或 'quit' 或按下 Ctrl+C 都可結束對話\n")

    while True:
        try:
            user_input = input("💬 請輸入 Prompt: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 感謝使用！再見！")
                break

            ask_gemini(client, user_input)

        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 偵測到結束指令，程式關閉。")
            break


if __name__ == "__main__":
    main()