from flask import Flask, render_template, request
import sqlite3
from datetime import date, timedelta, datetime
from helpers import get_coding_vals, get_book_vals, get_savings_vals, get_exercise_vals


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/progress", methods=["GET", "POST"])
def progress():
	if request.method == "POST":
		coding = float(request.form['coding'])
		reading = float(request.form['reading'])
		savings = float(request.form['savings'])
		exercise = float(request.form['exercise'])

		current_date = str(date.today())

		with sqlite3.connect('goal_tracker.db') as conn:
			c = conn.cursor()
			if coding > 0:
				c.execute('INSERT INTO progress (name, input_date, amount) VALUES (?, ?, ?)', ('CS/MATH', current_date, coding))
			if reading > 0:
				c.execute('INSERT INTO progress (name, input_date, amount) VALUES (?, ?, ?)', ('Reading', current_date, reading))
			if savings > 0:
				c.execute('INSERT INTO progress (name, input_date, amount) VALUES (?, ?, ?)', ('Savings', current_date, savings))
			if exercise > 0:
				c.execute('INSERT INTO progress (name, input_date, amount) VALUES (?, ?, ?)', ('Exercise', current_date, exercise))


	with sqlite3.connect('goal_tracker.db') as conn:
		c = conn.cursor()
		d = date.today()
		prior = d.replace(day=1) - timedelta(days=1)
		prior = prior.strftime('%Y-%m')
		new_week = d - timedelta(days=d.weekday())

		# Coding Values
		coding_vals = get_coding_vals(prior_date=prior, current_date=d, connection=c)

		# Books
		book_vals = get_book_vals(prior_date=prior, connection=c)

		# Exercise
		ex_vals = get_exercise_vals(new_week=new_week, connection=c)

		# Savings
		saving_vals = get_savings_vals(current_date=d, connection=c)

	return render_template("progress.html", 
							coding_vals=coding_vals, 
							book_vals=book_vals, 
							ex_vals=ex_vals,
							saving_vals=saving_vals
							)


@app.route("/modify")
def modify():
	return render_template("modify.html")


if __name__ == "__main__":
	app.run(debug=True 	)