from flask import Flask, request, jsonify
import requests
from datetime import datetime
import socket

app = Flask(__name__)

# ✅ Yahaan pe apni API keys aur expiry set karo
API_KEYS = {
    "freetrail": "2025-09-30",   # ye key 30 Sept 2025 tak valid hai
    "vip_user": "2025-10-15"     # ye key 15 Oct 2025 tak valid hai
}

# ✅ Ye wo original API hai jo tu hide karna chahta hai
ORIGINAL_API = "https://amaranthmagpie.onpella.app/api/number/lookup?number={}&key=1monthcyber"

@app.route("/swapiinfo", methods=["GET"])
def myapi():
    api_key = request.args.get("api_key")
    number = request.args.get("number")

    # 1. API Key check
    if not api_key or api_key not in API_KEYS:
        return jsonify({"success": False, "error": "❌ Invalid API Key"}), 401

    # 2. Expiry check
    expiry_date = datetime.strptime(API_KEYS[api_key], "%Y-%m-%d")
    if datetime.now() > expiry_date:
        return jsonify({"success": False, "error": "⏳ API Key Expired"}), 403

    # 3. Original API call
    try:
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
        "usage": "/swapiinfo?api_key=YOUR_KEY&number=9876543210"
    })


# ✅ Auto Free Port Finder
def find_free_port(start_port=5000, max_port=6000):
    for port in range(start_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("0.0.0.0", port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free ports found!")


if __name__ == "__main__":
    port = find_free_port()
    print(f"🚀 Flask running on port {port}")
    app.run(host="0.0.0.0", port=port)
