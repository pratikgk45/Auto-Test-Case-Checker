import sys
import requests
import subprocess
from lxml import html
from lxml import etree

contest_id = (sys.argv)[1]
contest_url = "http://codeforces.com/contest/"+contest_id

response = requests.get(contest_url)
if response.status_code != 200:
	sys.exit(0)

html_content = html.document_fromstring(response.text)
try:
	node = html_content.find_class("problems")[0]
except:
	sys.exit(0)

problem_list=[]
for i in range(1,len(node)):
	print(node[i][0].text_content().replace("\r","").replace("\n","").replace(" ",""))

sys.exit(1)