from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []  # ذخیره پیام‌ها موقتاً در حافظه

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    messages.append(data)
    return jsonify({"status": "received"}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run()
