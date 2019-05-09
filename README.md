Auto Test Case Checker
=====================
http://codeforces.com conducts programming contests. While participating in the contest, it would be better if we could check all the sample test cases by running a single command. This repository is going to help in that only.

Currently these scripts are only for programming in C++ (If you want to extend to others, modifying the scripts is quite easy).

Installation and Configuration
------------------------------
* Download this repository.
* Navigate to repository and give permission to files for execution
```bash
chmod +x gen.sh
chmod +x scripts/ver.sh
```
* Update the template.cpp file as needed. It's content will be initial content of each .cpp file created further.

How to Use
----------
Suppose you want to participate in http://codeforces.com/contest/1155

* Run './gen.sh'
* It will ask you contest ID, number of problems and test case import flag value. Enter these 3 space-separated integer values and execute.
* For this contest, Contest ID is 1155 and number of problems is 6. By doing this, you are creating folder with specified number of .cpp files and a test case folder.
* __If you are creating folder before the contest__ :
	- Number of problems will be specified in the respective blog of contest.
	- Contest ID can be seen in URL by clicking on contest registrants list link https://codeforces.com/contestRegistrants/1155 (list of people registered for contest, it is always present in rightmost column in contests lists https://codeforces.com/contests).
* __If you are creating folder after contest problems are released__ :
	- You can just go to https://codeforces.com/contest/1155 and see number of problems.
* Initially, script will only create folder with respective number of .cpp files whose content is the same as the template.cpp file which you have configured earlier and test case folder which is kept empty for now.
* __Test Case import Flag can be either 0 or 1__ :
	- If flag is kept 0, everything is already done :)
	- If flag is kept 1, script will try to import test cases for specified number of problems __for 5 times__. If any test case import fail, script will again try from first problem. After 5 attempts, even if test cases are not imported, script will terminate. For any given try, if test cases for all problems are imported, script will terminate.
* __You need to run gen.sh script command with Flag 1 atleast once to access test cases.__ For live contests, it is preferred to execute script before 5-10 seconds of the start of contest in such a way that __there should be atleast one attempt of import after release of problems__.
* Now, navigate to it by 'cd 1155'
* Write the solution for a problem (say D) in respective file (d.cpp).
* Run './ver.sh d' or './ver.sh D' to test your solution d.cpp with sample test cases for problem D imported from website.
