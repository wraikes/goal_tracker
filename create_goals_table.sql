--Create tables to record all goals, and starting progress.

DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS progress;


CREATE TABLE goals (
	goal_id integer PRIMARY KEY,
	name text NOT NULL UNIQUE,
	length text NOT NULL,
	amount real NOT NULL,
	amt_type text NOT NULL
);


INSERT INTO goals (name, length, amount, amt_type) VALUES 
	("CS/Math", "Monthly", 20, "hours"),
	("Reading", "Monthly", 1, "books"),
	("Savings", "None", 10000, "dollars")
;


CREATE TABLE progress (
	entry_id integer PRIMARY KEY,
	name text NOT NULL,
	input_date text NOT NULL,
	amount real NOT NULL
);


INSERT INTO progress (name, input_date, amount) VALUES
	("CS/MATH", date('now'), 0),
	("Readings", date('now'), 0),
	("Savings", date('now'), 250)
;


.save goal_tracker.db
