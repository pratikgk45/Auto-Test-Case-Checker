Auto Test Case Checker (ATCC)
=====================
http://codeforces.com conducts programming contests. While participating in the contest, it would be better if we could check all the sample test cases by running a single command. This repository is going to help in that only.

Currently these scripts are only for programming in C++ (If you want to extend to others, modifying the scripts is quite easy).

Installation and Configuration
------------------------------
1. Download this repository.
2. Navigate to repository and run following commands :
```bash
source init.sh
```
3. Update the template.cpp file as needed. It's content will be initial content of each .cpp file created further.

How to Use
----------
Suppose you want to participate or want to solve problems in http://codeforces.com/contest/1163

* Navigate to repository. Run '__source init.sh__' command.
* Then, run '__sol__' command. Enter Contest ID (say 1163 for this contest). Enter __space-separated__ problem IDs for problems you want to solve (say A B1 B2). If you want to solve all problems, keep this place blank and all problems will be imported, otherwise respective problems will be imported.
* Enter flag value (0 or 1) so as to download problem statements or not (0 - NO and 1 - YES).
* If problems are not released yet, program will terminate.
* If started, it will create a folder "cf_"contest_id (say cf_1163) containing .cpp files, one for each problem along with scripts (ver.sh and run.sh), Test case folder where all imported test cases will be placed and ps folder where all imported problem statements will be placed.
* If you want to see/solve problems __offline__, they are imported in '__ps__' folder in "cf_"contest_id folder.
* Now, navigate to contest folder by '__cd cf_1163__' command.
* Write the solution for a problem (say A) in respective file (A.cpp).
* Run '__ver a__' or '__ver A__' to test your solution A.cpp with sample test cases for problem A imported from website.
* To test your solution A.cpp with custom test case, run '__run a__' or '__run A__' command and get output by entering respective arguments. __Whole custom input should be placed in a single line__.
* If you get any error related to '__sol__', '__ver__' or '__run__' commands or about permission, refer to point 2 in 'Installation and Configuration' section.
