import sqlite3
from datetime import date, timedelta, datetime


def get_coding_vals(prior_date, current_date, connection):
	coding_vals = dict()

	code_current = connection.execute(
		'SELECT sum(amount) FROM progress WHERE input_date >= ? AND name == "CS/MATH"',
		(prior_date,)
		).fetchone()[0]
	coding_vals['current'] = code_current
	
	coding_vals['avg'] = round(code_current / current_date.day, 3)
	
	code_goal = connection.execute(
		'SELECT amount FROM goals WHERE name == "CS/MATH"'
		).fetchone()[0]
	coding_vals['goal'] = code_goal
	
	code_delta = code_goal - code_current
	coding_vals['delta'] = code_delta if code_delta > 0 else 'Goal Met!'

	return coding_vals


def get_book_vals(prior_date, connection):
	book_vals = dict()

	book_current = connection.execute(
		'SELECT sum(amount) FROM progress WHERE input_date >= ? AND name == "Reading"',
		(prior_date,)
		).fetchone()[0]
	book_vals['current'] = book_current
	
	book_goal = connection.execute(
		'SELECT amount FROM goals WHERE name == "Reading"'
		).fetchone()[0]
	book_vals['goal'] = book_goal

	return book_vals


def get_savings_vals(current_date, connection):
	saving_vals = dict()

	save_total = connection.execute(
		'SELECT sum(amount) FROM progress WHERE name == "Savings"'
		).fetchone()[0]
	saving_vals['total'] = save_total
	
	min_date = connection.execute(
		'SELECT min(input_date) FROM progress WHERE name == "Savings"'
		).fetchone()[0]
	min_date = datetime.strptime(min_date, "%Y-%m-%d")
	months = (current_date.year - min_date.year) * 12 + current_date.month - min_date.month + 1
	saving_vals['avg'] = round(save_total / months, 3)
	
	save_goal = connection.execute(
		'SELECT amount FROM goals WHERE name == "Savings"'
		).fetchone()[0]
	saving_vals['goal'] = save_goal
	
	save_delta = save_goal - save_total
	saving_vals['delta'] = save_delta if save_delta > 0 else 'Goal Met!'

	return saving_vals



def get_exercise_vals(new_week, connection):
	ex_vals = dict()

	ex_current = connection.execute(
		'SELECT sum(amount) FROM progress WHERE input_date >= ? AND name == "Exercise"',
		(new_week, )  #d.strftime("%W")
		).fetchone()[0]
	ex_vals['current'] = ex_current
	
	ex_goal = connection.execute(
		'SELECT amount FROM goals WHERE name == "Exercise"'
		).fetchone()[0]
	ex_vals['goal'] = ex_goal

	ex_vals['delta'] = 0 #ex_goal - ex_current

	return ex_vals

