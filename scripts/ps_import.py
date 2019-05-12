import sys
import os
import requests
import subprocess
from lxml import html
from lxml import etree
import pdfkit

contest_id = (sys.argv)[1]

task_id  = sys.argv[2]
task_url = "http://codeforces.com/contest/"+contest_id+"/problem/"+task_id

response = requests.get(task_url)
if response.status_code != 200:
	sys.exit(0)

# print("-> Response Code = "+str(response.status_code))
html_content = html.document_fromstring(response.text)
try:
	node = html_content.find_class("problemindexholder")[0]
except:
	sys.exit(0)

node=etree.tostring(node).decode('utf-8')
filename = "cf_"+contest_id+"/"+task_id+".html"
f = open(filename,'w')

css_file=os.path.abspath("scripts/style.css")
node="<script type='text/x-mathjax-config'>MathJax.Hub.Config({tex2jax: {inlineMath: [['$$$','$$$']], displayMath: [['$$$$$$','$$$$$$']]}});</script><script type='text/javascript' async src='https://assets.codeforces.com/mathjax/MathJax.js?config=TeX-AMS_HTML-full'></script><link rel='stylesheet' href='"+css_file+"'>"+node
f.write(node)
f.close()
config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
options = {
    'quiet': '',
    'javascript-delay' : '5000',
}
pdfkit.from_file(filename, "cf_"+contest_id+"/ps/"+task_id+".pdf", configuration=config, css=css_file, options=options)
os.remove(filename)
sys.exit(1)