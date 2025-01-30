import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route(‘/webhook’, methods=[‘POST’])
def webhook():
    try:
        data = request.get_json()  # Ensure JSON data is received
        if not data:
            return jsonify({“error”: “No JSON payload received”}), 400

        print(data)  # Log for debugging
        return jsonify({“status”: “success”}), 200  # Respond with success

    except Exception as e:
        print(f”Error: {e}”)  # Log errors
        return jsonify({“error”: “Invalid request”}), 400

# Expose app for Gunicorn
gunicorn_app = app

if __name__ == “__main__”:
    port = int(os.environ.get(“PORT”, 5000))  # Default to Railway-assigned port
    app.run(host=“0.0.0.0”, port=port)
