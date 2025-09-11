from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# ================== CONFIG ==================
ADMIN_SECRET = "swapi"  # Change for security

# ✅ Store API Keys (In-memory for now)
# Later you can shift to database
API_KEYS = {
    "lol": {"expiry": "2025-09-15", "rate_limit": 40},
    "vip_user": {"expiry": "2025-10-15", "rate_limit": 100},
    "MAHADEV": {"expiry": "2025-12-31", "rate_limit": None}  # Unlimited
}

# ✅ Usage tracker {api_key: {"count": int, "reset_time": datetime}}
usage_tracker = {}

# ✅ Original API (your provided one)
ORIGINAL_API = "https://thakurprojects.site/num-osint.php?number={}&Token=swapi1129"


# ================== FUNCTIONS ==================
def check_rate_limit(api_key, limit):
    """Rate limit checker"""
    if limit is None:  # Unlimited
        return True, None, None

    now = datetime.now()
    if api_key not in usage_tracker:
        usage_tracker[api_key] = {"count": 0, "reset_time": now + timedelta(hours=1)}

    tracker = usage_tracker[api_key]

    # Reset counter if time passed
    if now >= tracker["reset_time"]:
        tracker["count"] = 0
        tracker["reset_time"] = now + timedelta(hours=1)

    # If limit exceeded
    if tracker["count"] >= limit:
        return False, tracker["reset_time"], limit

    tracker["count"] += 1
    return True, tracker["reset_time"], limit - tracker["count"]


# ================== ROUTES ==================
@app.route("/")
def home():
    return jsonify({
        "message": "🚀 Welcome to Custom Number Info API",
        "usage_example": "/numbers/9876543210?api_key=freetrial",
        "note": "API Owner: @swapibhai"
    })


@app.route("/numbers/<number>", methods=["GET"])
def lookup_number(number):
    api_key = request.args.get("api_key")

    # Invalid key
    if not api_key or api_key not in API_KEYS:
        return jsonify({"success": False, "error": "❌ Invalid API Key"}), 401

    key_info = API_KEYS[api_key]

    # Expiry check
    expiry_date = datetime.strptime(key_info["expiry"], "%Y-%m-%d")
    if datetime.now() > expiry_date:
        return jsonify({"success": False, "error": "⏳ API Key Expired"}), 403

    # Rate limit check
    allowed, reset_time, remaining = check_rate_limit(api_key, key_info["rate_limit"])
    if not allowed:
        return jsonify({
            "success": False,
            "error": "🚫 Rate Limit Exceeded",
            "retry_after": reset_time.strftime("%H:%M:%S")
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


# ================== ADMIN ROUTES ==================
@app.route("/admin/add_key", methods=["POST"])
def add_key():
    admin_secret = request.args.get("admin_secret")
    if admin_secret != ADMIN_SECRET:
        return jsonify({"error": "❌ Unauthorized"}), 403

    data = request.get_json()
    api_key = data.get("api_key")
    expiry = data.get("expiry")
    rate_limit = data.get("rate_limit", None)

    if not api_key or not expiry:
        return jsonify({"error": "⚠️ api_key and expiry required"}), 400

    API_KEYS[api_key] = {
        "expiry": expiry,
        "rate_limit": rate_limit
    }
    return jsonify({"success": True, "message": f"✅ Key {api_key} added"})


@app.route("/admin/remove_key", methods=["POST"])
def remove_key():
    admin_secret = request.args.get("admin_secret")
    if admin_secret != ADMIN_SECRET:
        return jsonify({"error": "❌ Unauthorized"}), 403

    data = request.get_json()
    api_key = data.get("api_key")

    if api_key in API_KEYS:
        del API_KEYS[api_key]
        return jsonify({"success": True, "message": f"🗑️ Key {api_key} removed"})
    return jsonify({"error": "⚠️ Key not found"}), 404


@app.route("/admin/list_keys", methods=["GET"])
def list_keys():
    admin_secret = request.args.get("admin_secret")
    if admin_secret != ADMIN_SECRET:
        return jsonify({"error": "❌ Unauthorized"}), 403

    return jsonify({"api_keys": API_KEYS})


# ================== MAIN ==================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
