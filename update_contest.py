import sqlite3
import sys
import requests
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup

def get_contest_info(contest_id):
	contest_info = {}
	url = "https://codeforces.com/contest/"+contest_id
	response = requests.get(url)
	if response.status_code != 200:
		sys.exit(0)
	html_content = html.document_fromstring(response.content)
	node=etree.tostring(html_content).decode('utf-8')
	soup = BeautifulSoup(node,'lxml')
	contest_info['contest_name'] = soup.findAll("th", {"class" : "left"})[0].text
	node = html_content.find_class("problems")[0]
	node=etree.tostring(html_content).decode('utf-8')
	soup = BeautifulSoup(node,'lxml')
	for i in soup.findAll("tr"):
		try:
			problem_id = i.a.text.replace(" ","").replace("\r","").replace("\n","")
			problem_name = i.div.div.a.text.replace("\r","").replace("\n","")
			contest_info[problem_id] = problem_name
		except:
			pass
	return contest_info

conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()

contest_id = (sys.argv)[1]
problem_list_1 = (sys.argv)[2:]
problem_list_2 = list(cur.execute('SELECT problem_id FROM problems WHERE contest_id = '+str(contest_id)).fetchall())
problem_list_2 = [i[0] for i in problem_list_2]

problem_list = list(set(problem_list_1) - set(problem_list_2))
problem_list.sort()

contest_info = get_contest_info(contest_id)
for problem in problem_list:
	cur.execute('INSERT INTO problems(contest_id, contest_name, problem_id, problem_name) VALUES('+str(contest_id)+', "'+contest_info['contest_name']+'", "'+problem+'", "'+contest_info[problem]+'")')
	conn.commit()

conn.close()