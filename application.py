from flask import Flask, render_template, request
import sqlite3
from datetime import date


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/progress", methods=["GET", "POST"])
def progress():
	if request.method == "POST":
		coding = float(request.form['coding'])
		reading = float(request.form['reading'])
		savings = float(request.form['savings'])

		current_date = str(date.today())

		with sqlite3.connect('goal_tracker.db') as conn:
			c = conn.cursor()
			if coding > 0:
				c.execute('INSERT INTO progress (name, input_date, amount) VALUES (?, ?, ?)', ('CS/MATH', current_date, coding))
			if reading > 0:
				c.execute('INSERT INTO progress (name, input_date, amount) VALUES (?, ?, ?)', ('Reading', current_date, reading))
			if savings > 0:
				c.execute('INSERT INTO progress (name, input_date, amount) VALUES (?, ?, ?)', ('Savings', current_date, savings))

	with sqlite3.connect('goal_tracker.db') as conn:
		c = conn.cursor()
		coding_vals = dict()
		coding_vals['total'] = c.execute('SELECT sum(amount) FROM progress WHERE name == "CS/MATH"')
		coding_vals['current'] = 'placeholder'
		coding_vals['avg'] = 'placeholder'
		coding_vals['goal'] = 'placeholder'
		coding_vals['delta'] = 'placeholder'

	return render_template("progress.html", coding_vals=coding_vals)


@app.route("/modify")
def modify():
	return render_template("modify.html")


if __name__ == "__main__":
	app.run(debug=True 	)