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
Suppose you want to participate or want to solve problems in http://codeforces.com/contest/1155

* Navigate to repository. Run '__source init.sh__' command.
* Then, run '__sol__' command. Enter Contest ID (say 1155 for this contest). Enter __space-separated__ problem IDs for problems you want to solve (say A B1 B2). Test case import for corresponding problems will take place. If you want to solve all problems, keep this place blank and all problems will be imported.
* If problems are not released yet, program will terminate.
* If started, it will create a folder "cf_"contest_id (say cf_1155) containing .cpp files, one for each problem along with scripts (ver.sh and run.sh) and Test case folder where all imported test cases will be placed.
* Now, navigate to contest folder by '__cd cf_1155__' command.
* Write the solution for a problem (say D) in respective file (d.cpp).
* Run '__ver d__' or '__ver D__' to test your solution d.cpp with sample test cases for problem D imported from website.
* To test your solution d.cpp with custom test case, run '__run d__' or '__run D__' command and get output by entering respective arguments. __Custom input should be placed in a single line__.
* If you get any error related to '__sol__', '__ver__' or '__run__' commands or about permission, refer to point 2 in 'Installation and Configuration' section.