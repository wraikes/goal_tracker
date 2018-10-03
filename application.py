from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/progress")
def progress():
	return render_template("progress.html")


@app.route("/modify")
def modify():
	return render_template("modify.html")

