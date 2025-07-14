from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

TOGETHER_API_KEY = "tgp_v1_7UHYtm5aqC5nJ_I66vemW5--NSZIIQA8SFXqI2xCFqg"
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message')

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",  # Use any Together model
        "messages": [
            {"role": "system", "content": "You are an AI health assistant. Ask clarifying questions based on symptoms and suggest next steps."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(TOGETHER_API_URL, headers=headers, json=payload)
    result = response.json()

    reply = result["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
