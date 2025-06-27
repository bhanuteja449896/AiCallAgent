import sys
import requests

def get_llm_reply(prompt, user_input):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "phi3",  # or "mistral" etc.
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 128,
        "temperature": 0.2
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompt = "You are my assistant. If a delivery person calls, tell them: 'Please keep the package near the blue chair at the main door.'"
    user_input = sys.argv[1]
    print(get_llm_reply(prompt, user_input)) 