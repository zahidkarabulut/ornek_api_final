from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Merhaba Dünya!"})

@app.route('/users')
def users():
    return jsonify([
        {"id": 1, "name": "Mehmet Zahit Karabulut"},
        {"id": 2, "name": "Zeynep Sare Karabulut"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)