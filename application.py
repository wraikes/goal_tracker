from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/progress", methods=["GET", "POST"])
def progress():
	if request.method == "POST":
		with sqlite3.connect('progress.db') as conn:
			c = conn.cursor()
			if float(request.form['coding']) > 0:
				c.execute('INSERT INTO progress (name, date, amount) VALUES (?, ?, ?)', ('CS/MATH', date(now), request.form['coding']))
			if float(request.form['reading']) > 0:
				c.execute('INSERT INTO progress (name, date, amount) VALUES (?, ?, ?)', ('Reading', date(now), request.form['reading']))
			if float(request.form['savings']) > 0:
				c.execute('INSERT INTO progress (name, date, amount) VALUES (?, ?, ?)', ('Savings', date(now), request.form['savings']))

	return render_template("progress.html")


@app.route("/modify")
def modify():
	return render_template("modify.html")


if __name__ == "__main__":
	app.run(debug=True 	)