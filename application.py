from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/progress", methods=["GET", "POST"])
def progress():
	if request.form == 'post':
		pass		

	return render_template("progress.html")


@app.route("/modify")
def modify():
	return render_template("modify.html")


if __name__ == "__main__":
	app.run(debug=True 	)