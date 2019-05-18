import sys
import os
import requests
import subprocess
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
import base64

def get_image_file_as_base64_data(filepath):
    with open(filepath, 'rb') as image_file:
    	return base64.b64encode(image_file.read())

contest_id = (sys.argv)[1]

task_id  = sys.argv[2]
task_url = "http://codeforces.com/contest/"+contest_id+"/problem/"+task_id

response = requests.get(task_url)
if response.status_code != 200:
	sys.exit(0)

# print("-> Response Code = "+str(response.status_code))
html_content = html.document_fromstring(response.content)
node=etree.tostring(html_content).decode('utf-8')
filename = "contests/cf_"+contest_id+"/ps/"+task_id+".html"
f = open(filename,'w')
soup = BeautifulSoup(node,'lxml')
try:
	node = html_content.find_class("problemindexholder")[0]
except:
	sys.exit(0)
node=etree.tostring(node).decode('utf-8')

node="<button onclick='go_to_top_fun()' id='go_to_top_btn' title='Go to Top'>&#10148</button>"+node
node="</ul></div></div><script>$(document).ready(function(){$('#tag_btn').click(function(){$('#tags').slideToggle();});});</script>"+node
node1=""
prob_diff=0
for tag in soup.findAll("span",{"class":"tag-box"}):
	if tag['title'] == "Difficulty":
		prob_diff = int(tag.text.replace(" ","").replace("\r","").replace("\n","")[1:])
	else:
		node1 = node1+"<li title='"+tag['title']+"'>"+tag.text+"</li>"
if len(node1) == 0 and prob_diff == 0:
	node1 = "<li style='border:none;color:#d99;font-size:14px;'>No tags imported yet. Please update problem statement by calling <a href='https://github.com/pratikgk45/atcc#how-to-use' style='color:#9d9;font-weight:bold;' target='_blank'>sol command</a> (refer README). If still not imported, they are not published yet.</li>"
	node = node1 + node
elif len(node1) == 0:
	node1 = "<li><b>Problem Difficulty :</b> "+str(prob_diff)+"</li>"
	node = node1 + node
elif prob_diff == 0:
	node = node1 + node
else:
	node = node1+"<br><li  style='border: none;'><b>Problem Difficulty :</b> "+str(prob_diff)+"</li>"+node

node="<div id='tags'><ul id='tag_list'>"+node
node="<div class='second-level-menu'><ul class='second-level-menu-list'><li><a href='https://codeforces.com/contest/"+contest_id+"' target='_blank'>Link to Contest</a></li><li><a href='https://codeforces.com/contest/"+contest_id+"/problem/"+task_id+"' target='_blank'>Link to Problem</a></li><li><a href='https://codeforces.com/contest/"+contest_id+"/submit/"+task_id+"/' target='_blank'>Submit Code</a></li><li><a href='https://codeforces.com/contest/"+contest_id+"/my' target='_blank'>My Submissions</a></li><li><a href='https://codeforces.com/contest/"+contest_id+"/status/"+task_id+"' target='_blank'>Problem Status</a></li><li><a href='https://codeforces.com/contest/"+contest_id+"/hacks' target='_blank'>Hacks</a></li><li><a href='https://codeforces.com/contest/"+contest_id+"/room/0' target='_blank'>Room</a></li><li><a href='https://codeforces.com/contest/"+contest_id+"/standings' target='_blank'>Standings</a></li><li><a id='tag_btn'>Tags</a></li></ul>"+node
node="<script>window.onscroll = function(){scrollFunction()};function scrollFunction(){if (document.body.scrollTop > 60 || document.documentElement.scrollTop > 60)document.getElementById('go_to_top_btn').style.display='block';else document.getElementById('go_to_top_btn').style.display = 'none';}function go_to_top_fun(){document.body.scrollTop = 0;document.documentElement.scrollTop = 0;}</script>"+node
mathjax_file="../static/MathJax/MathJax.js?config=TeX-AMS_HTML-full"
css_file_1="../static/css/style.css"
css_file_2="../static/css/menu.css"
jquery_file="../static/js/jquery-2.1.0.min.js"
node="<script type='text/x-mathjax-config'>MathJax.Hub.Config({tex2jax: {inlineMath: [['$$$','$$$']], displayMath: [['$$$$$$','$$$$$$']]}});</script><script src='"+jquery_file+"'></script><script type='text/javascript' async src='"+mathjax_file+"'></script><link rel='stylesheet' href='"+css_file_1+"'><link rel='stylesheet' href='"+css_file_2+"'>"+node
node=node.replace('src="/','src="https://codeforces.com/')
node=node.replace('href="/','href="https://codeforces.com/')
soup = BeautifulSoup(node,'lxml')
images = []
for img in soup.findAll('img'):
    file_name = img['src']
    base_file_name = os.path.basename(file_name)
    images.append(base_file_name)
    img_data = requests.get(file_name).content
    with open("contests/cf_"+contest_id+"/"+base_file_name, 'wb') as handler:
    	handler.write(img_data)
    base_file_name=os.path.abspath("contests/cf_"+contest_id+"/"+base_file_name)
    img['src']="data:image/png;base64,"+str(get_image_file_as_base64_data(base_file_name).decode('utf-8'))
node = str(soup)
f.write(node)
f.close()
for img in images:
	if os.path.isfile("contests/cf_"+contest_id+"/"+img):
		os.remove("contests/cf_"+contest_id+"/"+img)
sys.exit(1)