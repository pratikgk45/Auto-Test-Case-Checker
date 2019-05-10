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
* Enter Contest ID (say 1155 for this contest).
* It will create folder "cf_"contest_id (say cf_1155) containing empty test case folder and ver.sh script.
* Exactly 5 attempts will be made. In each attempt, script will try to import problem list and test cases which will be available only if problems are released. If during or before any attempt, problems are released, test cases will be imported and program will terminate. If not, even if import is unsuccessful, it will automatically terminate after 5 attempts.
* So, after a successful attempt, we will have a folder with .cpp files, one for each problem along with Test case folder where all imported test cases will be placed.
* If all attempts fail, you need to run script again expecting that problems will be released in between.
* __For live contests, you need to run gen.sh script command atleast once in such a way that problems will be released before any attempt made.__
* Now, navigate to folder by 'cd cf_1155'
* Write the solution for a problem (say D) in respective file (d.cpp).
* Run './ver.sh d' or './ver.sh D' to test your solution d.cpp with sample test cases for problem D imported from website.
