# app.py
import requests
from flask import Flask, Response

app = Flask(__name__)

# Apna GitHub raw file URL yahan daal
# Example: https://raw.githubusercontent.com/username/repo/main/tool.py
GITHUB_RAW_URL = "https://raw.githubusercontent.com/swapipapabolte/Bg-remover-bot/refs/heads/main/2k11_file_dec%20(2).py"

@app.route("/get", methods=["GET"])
def get_tool():
    try:
        resp = requests.get(GITHUB_RAW_URL)
        if resp.status_code == 200:
            return Response(resp.text, mimetype="text/plain")
        else:
            return {"error": "Failed to fetch GitHub file"}, 500
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
