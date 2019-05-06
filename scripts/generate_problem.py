import sys
import requests
import subprocess
from lxml import html
from lxml import etree

contest_id = (sys.argv)[1]

task_id  = sys.argv[2]
task_url = "http://codeforces.com/contest/"+contest_id+"/problem/"+task_id

response = requests.get(task_url)
if response.status_code != 200:
	print "Problem URL Fetching Failed"
	sys.exit()

# print "-> Response Code = "+str(response.status_code)
html_content = html.document_fromstring(response.text)
try:
	node = html_content.find_class("sample-test")[0]
except:
	print "-> Test Case Fetching Failed"
	quit()

def filter_node(node,in_or_out):
	node = node.getchildren()[1]
	node = etree.tostring(node, pretty_print=True)
	node = node.replace("<pre>","")
	node = node.replace("</pre>","")
	node = node.replace("<br/>","\n")
	# print node
	filename = "cf_"+contest_id+'/test_cases/'+task_id+'_'+in_or_out+'_'+str(test_id) 
	f = file(filename,'w')
	f.write(node)
	f.close()
	subprocess.call("sed -i '/^$/d' "+filename,shell=True)

num_samples = len(node.getchildren())/2
f = file(("cf_"+contest_id+'/test_cases/'+task_id+'_num_samples'),'w')
f.write(str(num_samples))
for test_id in range(num_samples):
	test_input  = node[test_id*2]
	test_input = filter_node(test_input,'in')
	test_output = node[test_id*2+1]
	test_output = filter_node(test_output,'out')
print "-> Test Cases Successfully Imported"