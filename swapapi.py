from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# ---- API Key Config ----
VALID_KEYS = {
    "swapipy": {"expiry": "2025-09-23"},   # free trial key
    "vip123": {"expiry": "2026-01-01"}     # premium key
}

# ---- Request Counter ----
request_count = 0

# ---- Middleware for Key Check ----
def check_api_key(api_key):
    if not api_key or api_key not in VALID_KEYS:
        return {"error": "Invalid or missing API key"}, False

    today = datetime.today().strftime("%Y-%m-%d")
    if today > VALID_KEYS[api_key]["expiry"]:
        return {"error": "API key expired"}, False

    return None, True

# ---- Main Route ----
@app.route("/info", methods=["GET"])
def info():
    global request_count
    api_key = request.args.get("api_key")
    mobile = request.args.get("mobile")

    error, ok = check_api_key(api_key)
    if not ok:
        return jsonify(error), 403

    if not mobile:
        return jsonify({"error": "Missing mobile number"}), 400

    try:
        # Call your existing API
        url = f"https://flipcartstore.serv00.net/INFO.php?api_key=chxInfo&mobile={mobile}"
        response = requests.get(url)
        data = response.json()

        # Increase counter
        request_count += 1

        return jsonify({
            "credit": "Api Credit @swapibhai",
            "data": data
        })
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# ---- Secret Stats Route ----
@app.route("/dusts-stats", methods=["GET"])
def stats():
    secret = request.args.get("secret")
    if secret != "swapisecret":   # yaha apna secret dalna
        return jsonify({"error": "Unauthorized"}), 403

    return jsonify({
        "total_requests": request_count,
        "valid_keys": list(VALID_KEYS.keys())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
