--Create tables to record all goals, and starting progress.

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
	date text NOT NULL,
	amount read NOT NULL
);


INSERT INTO progress (name, date, amount) VALUES
	("CS/MATH", datetime('now'), 0),
	("Readings", datetime('now'), 0),
	("Savings", datetime('now'), 250)
;


.save goals.db
.save progress.db
.quit

