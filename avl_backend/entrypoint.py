from flask import Flask, request, jsonify
import sys
import json
import hashlib

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
	if request.method == "POST":

		jsonObject = request.json
		message = jsonObject["md5"]

		h = hashlib.new("md5")
		h.update(str.encode(message))
		hashed = h.hexdigest()

		return jsonify(hashed)
	else:
		return "Page used for md5 hashing"

if __name__ == "__main__":
	app.run(debug=True)