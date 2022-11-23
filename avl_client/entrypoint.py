from flask import Flask, render_template, request
import requests
import sys
import json

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
	return render_template("index.html")

@app.route("/hash", methods=["POST", "GET"])
def hash():
	if request.method == "POST":

		config = readConfig()

		client_url = config["clientApi"]
		backend_url = config["backendApi"]
		try:
		    response = requests.get(client_url).text
		    print(response)
		    myobj = {'md5': response}
		except:
		    print("ERROR: Failed to establish connection to client service")

		hash_output = requests.post(backend_url, json = myobj).text

		return hash_output
	else:
		return render_template("request.html")

def readConfig():
	with open("configs/config.json", "r") as f:
		file = json.load(f)
		return file

if __name__ == "__main__":
	app.run(debug=True)
