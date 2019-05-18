import sqlite3
import os

conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS problems')
cur.execute('CREATE TABLE problems (contest_id INT NOT NULL, contest_name TEXT, problem_id CHAR(10) NOT NULL, problem_name TEXT, CONSTRAINT Problem PRIMARY KEY(contest_id, problem_id) )')
conn.commit()

conn.close()