import openai
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

# OpenAI API キーを設定します
openai.api_key = "yourkey"

# 音声認識オブジェクトを作成します
recognizer = sr.Recognizer()

# マイクを使って音声をキャプチャします
with sr.Microphone() as source:
    print("話してください...")
    audio_data = recognizer.listen(source)
    print("音声を認識中...")

# ユーザーの発話履歴を保存します
conversation_history = []

while True:
    try:
        # マイクを使って音声をキャプチャします
        with sr.Microphone() as source:
            print("話してください...")
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            print("音声を認識中...")

        # 音声をテキストに変換します
        input_text = recognizer.recognize_google(audio_data, language="en")
        print("あなたが言ったこと: " + input_text)
        conversation_history.append(f"対話者A: {input_text}\n")

        prompt = "".join(conversation_history[-4:]) + "対話者B: Improve the following English expression by the user: '{}'\n".format(input_text)

        # OpenAI API による応答の取得
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )

        improved_text = response.choices[0].text.strip()
        print("ChatGPT からの改善提案: " + improved_text)
        conversation_history.append(f"対話者B: {improved_text}\n")

        # 応答を音声に変換して再生します
        tts = gTTS(text=improved_text, lang="en")
        tts.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3")

    except sr.UnknownValueError:
        print("音声認識エラー: 音声を理解できませんでした。")

    except sr.RequestError as e:
        print("音声認識エラー: サービスに接続できませんでした; {0}".format(e))

    except KeyboardInterrupt:
        print("\n終了します。")
        break
