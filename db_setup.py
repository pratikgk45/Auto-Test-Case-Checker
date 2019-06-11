import sqlite3
import os
import glob
import shutil
import sys

confirm = input("Are you sure you want to delete all contest data ? [y/n] : ")
if(confirm == 'n'):
	sys.exit()
conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS problems')
cur.execute('CREATE TABLE problems (contest_id INT NOT NULL, contest_name TEXT, problem_id CHAR(10) NOT NULL, problem_name TEXT, CONSTRAINT Problem PRIMARY KEY(contest_id, problem_id) )')
conn.commit()
conn.close()

dir_list = glob.iglob(os.path.join(os.getcwd()+"/contests","cf_*"));
for dir in dir_list:
	if os.path.isdir(dir):
		shutil.rmtree(dir)

print("Data successfully deleted")