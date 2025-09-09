from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# ✅ API keys + expiry date + rate limit
# rate_limit = None  -> unlimited
API_KEYS = {
    "freetrail": {"expiry": "2025-09-10", "rate_limit": 40},
    "vip_user": {"expiry": "2025-10-15", "rate_limit": 100},
    "HexAbhi": {"expiry": "2025-10-05", "rate_limit": None}
}

# ✅ Original API
ORIGINAL_API = "https://amaranthmagpie.onpella.app/api/number/lookup?number={}&key=1monthcyber"

# ✅ Usage tracker
usage_tracker = {}  # {api_key: {"count": int, "reset_time": datetime}}


def check_rate_limit(api_key, limit):
    # Unlimited case
    if limit is None:
        return True, None, None  

    now = datetime.now()

    if api_key not in usage_tracker:
        usage_tracker[api_key] = {"count": 0, "reset_time": now + timedelta(hours=1)}

    tracker = usage_tracker[api_key]

    # Agar reset time cross ho gaya → reset counter
    if now >= tracker["reset_time"]:
        tracker["count"] = 0
        tracker["reset_time"] = now + timedelta(hours=1)

    # Agar limit cross kar gaya
    if tracker["count"] >= limit:
        return False, tracker["reset_time"], limit  

    # Otherwise, request allow karo
    tracker["count"] += 1
    return True, tracker["reset_time"], limit - tracker["count"]


@app.route("/numbers/<number>", methods=["GET"])
def lookup_number(number):
    api_key = request.args.get("api_key")

    # Agar API key missing
    if not api_key or api_key not in API_KEYS:
        return jsonify({"success": False, "error": "❌ Invalid API Key"}), 401

    key_info = API_KEYS[api_key]

    # Expiry check
    expiry_date = datetime.strptime(key_info["expiry"], "%Y-%m-%d")
    if datetime.now() > expiry_date:
        return jsonify({"success": False, "error": "⏳ API Key Expired"}), 403

    # ✅ Rate limit check
    allowed, reset_time, remaining = check_rate_limit(api_key, key_info["rate_limit"])
    if not allowed:
        return jsonify({
            "success": False,
            "error": "🚫 Rate Limit Exceeded",
            "message": f"Try again after {reset_time.strftime('%H:%M:%S')}"
        }), 429

    try:
        # Call original API
        response = requests.get(ORIGINAL_API.format(number), timeout=20)
        data = response.json()

        return jsonify({
            "success": True,
            "number": number,
            "data": data.get("data", {}),
            "remaining_requests": remaining if remaining is not None else "∞",
            "reset_at": reset_time.strftime("%Y-%m-%d %H:%M:%S") if reset_time else "∞"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/")
def home():
    return jsonify({
        "message": "🚀 Welcome to My Custom Number Info API",
        "usage": "https://your-app-name.onrender.com/numbers/9876543210?api_key=freetrail",
        "note": "Api Owner:- @swapibhai"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
