import requests
from flask import Flask, make_response, request, jsonify
app = Flask(__name__)


@app.route("/lonpy", methods=["POST"])
def lonpy():
    payload = request.get_json()
    url = "https://lotsofnames.navicore.tech/names"
    resp = requests.post(url, json=payload)
    return jsonify(resp.json())


@app.route("/")
def hello():
    return make_response("""\
<!DOCTYPE html>
<meta charset="utf-8">
<title>Flask is fun</title>
<img src="flask.png" alt="Flask">""")


if __name__ == "__main__":
    app.run()
