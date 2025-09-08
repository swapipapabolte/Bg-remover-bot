from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# ✅ API keys + expiry date
API_KEYS = {
    "freetrail": "2025-09-10",
    "vip_user": "2025-10-15"
}

# ✅ Original API
ORIGINAL_API = "https://amaranthmagpie.onpella.app/api/number/lookup?number={}&key=1monthcyber"


@app.route("/numbers/<number>", methods=["GET"])
def lookup_number(number):
    # API key from query string
    api_key = request.args.get("api_key")

    # Agar API key missing
    if not api_key or api_key not in API_KEYS:
        return jsonify({"success": False, "error": "❌ Invalid API Key"}), 401

    # Expiry check
    expiry_date = datetime.strptime(API_KEYS[api_key], "%Y-%m-%d")
    if datetime.now() > expiry_date:
        return jsonify({"success": False, "error": "⏳ API Key Expired"}), 403

    try:
        # Call original API
        response = requests.get(ORIGINAL_API.format(number), timeout=20)
        data = response.json()

        return jsonify({
            "success": True,
            "number": number,
            "data": data.get("data", {})
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/")
def home():
    return jsonify({
        "message": "🚀 Welcome to My Custom Number Info API",
        "usage": "https://your-app-name.onrender.com/numbers/9876543210?api_key=freetrail"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
