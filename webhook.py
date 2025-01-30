from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Keep-Alive Route
@app.route("/", methods=["GET"]) 
def home():
    return “Webhook is running!”, 200

# Webhook Route
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()  # Ensure JSON data is received
        if not data:
            return jsonify({“error”: “No JSON payload received”}), 400

        print(data)  # Log the request payload for debugging
        return jsonify({“status”: “success”}), 200  # Respond with a success message

    except Exception as e:
        print(f”Error: {e}”)  # Log any errors
        return jsonify({“error”: “Invalid request”}), 400

# Expose the app variable for Gunicorn
gunicorn_app = app

if __name__ == “__main__”:
    port = int(os.environ.get(“PORT”, 5000))  # Use Railway's dynamic port
    app.run(host=“0.0.0.0", port=port)
