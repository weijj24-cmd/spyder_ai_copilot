import os
import sys
# 先印出標題，讓使用者知道程式已經在跑了
print("==========================================")
print("🚀 Gemini AI 程式開發助手 (CLI 工具)")
print("==========================================")
print("⏳ 正在載入系統模組，請稍候...\n")

# 放在這裡 import，讓畫面先呈現出來
from google import genai

def get_api_key():
    # 優先讀取環境變數，若無則提示使用者輸入
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("🔑 未檢測到環境變數 GEMINI_API_KEY")
        api_key = input("請貼上您的 Gemini API Key: ").strip()
    return api_key

def ask_gemini(client, prompt: str):
    print("\n🤖 Gemini 思考中...\n")
    sys_instruction = "你是一個專業的 Python 程式輔助 AI。請針對使用者的需求，優先提供精簡、正確且附帶關鍵註解的 Python 程式碼。"

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config={"system_instruction": sys_instruction},
        )
        print("====== 生成結果 ======\n")
        print(response.text)
        print("\n" + "=" * 22 + "\n")
    except Exception as e:
        print(f"❌ 發生錯誤：{e}\n")

def main():
    print("==========================================")
    print("🚀 Gemini AI 程式開發助手 (CLI 工具)")
    print("==========================================\n")
    
    api_key = get_api_key()
    if not api_key:
        print("❌ 未提供 API Key，程式即將關閉。")
        return
        
    client = genai.Client(api_key=api_key)

    print("\n💡 輸入你的需求（例如：『幫我用 pandas 讀取 csv』）")
    print("🚪 輸入 'exit' 或 'quit' 或按下 Ctrl+C都可結束對話")

    while True:
        try:
            user_input = input("💬 請輸入 Prompt: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 已結束 Gemini AI 助手。")
                break
            if not user_input:
                continue
            ask_gemini(client, user_input)
        except KeyboardInterrupt:
            print("\n\n👋 已強制停止 AI 助手。")
            break

if __name__ == "__main__":
    main()