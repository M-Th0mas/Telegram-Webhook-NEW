from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()  # Ensure JSON data is received
        if not data:
            return jsonify({"error": "No JSON payload received"}), 400

        print(data)  # Log the request payload for debugging
        return jsonify({"status": "success"}), 200  # Respond with a success message

    except Exception as e:
        print(f"Error: {e}")  # Log any errors
        return jsonify({"error": "Invalid request"}), 400

# Expose the app variable for Gunicorn
app = app  # Make sure Gunicorn can find this
