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

		client_url = 'http://avl-client-api:5010/hash'
		backend_url = 'http://avl-backend-api:5020/'
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

if __name__ == "__main__":
	app.run(debug=True)
