Auto Test Case Checker (ATCC)
=====================
http://codeforces.com conducts programming contests. While participating in the contest or while upsolving, it would be better if we could check all the sample test cases by running a single script. Also, we may need to solve problems without internet connection and check solutions on sample test cases. This repository is going to help in that only.

Currently these scripts are only for programming in C++ (If you want to extend to others, modifying the scripts is quite easy).

Installation and Configuration
------------------------------
1. Download/clone this repository.
2. Refer to [requirements.txt](./requirements.txt)
3. Navigate to repository and run following commands in given sequence :
```bash
cd scripts
mkdir MathJax-2.7.3
git clone https://github.com/mathjax/MathJax.git ./MathJax-2.7.3/
cd ..
source init.sh
```
4. Update the template.cpp file as needed. It's content will be initial content of each .cpp file created further.

How to Use
----------
Suppose you want to participate or want to solve problems in http://codeforces.com/contest/1163

* Navigate to repository. Run __source init.sh__ command.
* Then, run __sol__ command. Enter Contest ID (say 1163 for this contest). Enter __space-separated__ problem IDs for problems you want to solve (say A B1 B2). __If you want to solve all problems, keep this place blank__ and all problems will be imported, otherwise respective problems will be imported.
* Enter flag value (0 or 1) so as to download problem statements or not (0 - NO and 1 - YES).
* If problems are not released yet, program will terminate.
* If started, it will create a folder "cf_"contest_id (say cf_1163) containing .cpp files, one for each problem along with scripts (ver.sh and run.sh), Test case folder where all imported test cases will be placed and ps folder where all imported __html__ problem statements will be placed.
* If you want to see/solve problems __offline__, they will be available(if imported) in __ps__ folder in "cf_"contest_id folder.
* Now, navigate to contest folder by __cd cf_1163__ command.
* Write the solution for a problem (say A) in respective file (A.cpp).
* Run __ver a__ or __ver A__ to test your solution A.cpp with sample test cases for problem A imported from website.
* To test your solution A.cpp with custom test case, run __run a__ or __run A__ command and get output by entering respective arguments. __Whole custom input should be placed in a single line__.
* If you get any error related to __sol__, __ver__ or __run__ commands or about permission, refer to point 2 in 'Installation and Configuration' section.

Note
----
* You are allowed to call __sol__ any number of times for single contest. Everytime, test cases and problem statements will be created/updated for respective problems. __.cpp files will not be updated if they already exists__.
* It is possible that due to bad network or some reason, program may terminate throwing an error or take longer than expected. That time, it is advised to terminate the program and try again with same procedure follwed before.
* Tags present in problem statements are updated only when they are imported again using __sol__ command.