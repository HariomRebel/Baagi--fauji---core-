import os
import requests
import sys

# GitHub के गुप्त तहखाने से चाबी उठाना
API_KEY = os.getenv('GEMINI_API_KEY')
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def ask_rebel(question):
    payload = {
        "contents": [{"parts": [{"text": f"You are a rebel AI friend. Answer this like a human friend in Hindi: {question}"}]}]
    }
    response = requests.post(URL, json=payload)
    if response.status_code == 200:
        print(response.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        print("सिस्टम में गड़बड़ है, चाबी चेक कर!")

if __name__ == "__main__":
    # जो भी हम Issue में लिखेंगे, वो यहाँ आएगा
    user_input = sys.argv[1] if len(sys.argv) > 1 else "नमस्ते"
    ask_rebel(user_input)
