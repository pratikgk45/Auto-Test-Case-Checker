from flask import Flask, render_template, redirect, request
import os
import sqlite3 as sql

port = 5000
app = Flask(__name__, template_folder="contests")

@app.route('/')
def index():
	conn = sql.connect("sqlite.db")
	conn.row_factory = sql.Row
	cur = conn.cursor()
	cur.execute("SELECT contest_id, contest_name FROM contests ORDER BY update_time DESC")
	rows = cur.fetchall()
	return render_template('contest_index.html', contests=rows)

@app.route('/<contest_id>')
def contest_route(contest_id):
	conn = sql.connect("sqlite.db")
	conn.row_factory = sql.Row
	cur = conn.cursor()
	cur.execute("SELECT contest_name FROM contests WHERE contest_id='"+str(contest_id)+"'")
	rows = cur.fetchall()
	try:
		contest_name = rows[0][0]
	except:
		return render_template('404.html')
	cur.execute("SELECT problem_id, problem_name FROM problems WHERE contest_id='"+str(contest_id)+"'")
	rows = cur.fetchall()
	if len(rows)==0:
		return render_template('404.html')
	return render_template('problem_index.html', contest_name=contest_name, contest_id=contest_id, problems=rows)

@app.route('/<contest_id>/<task_id>')
def task_route(contest_id, task_id):
	conn = sql.connect("sqlite.db")
	conn.row_factory = sql.Row
	cur = conn.cursor()
	cur.execute("SELECT * FROM problems WHERE contest_id='"+str(contest_id)+"' AND problem_id='"+str(task_id)+"'")
	rows = cur.fetchall()
	if len(rows)==0:
		return render_template('404.html')
	return render_template('cf_'+contest_id+'/ps/'+task_id+'.html')

@app.route('/<contest_id>/<task_id>/submit')
def submit(contest_id, task_id):
	response = os.popen("python3 static/submit.py "+contest_id+" "+task_id).read()
	return response

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

if __name__ == '__main__':
	app.run(host='127.0.0.1',port=port,debug=True)