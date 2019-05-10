Auto Test Case Checker
=====================
http://codeforces.com conducts programming contests. While participating in the contest, it would be better if we could check all the sample test cases by running a single command. This repository is going to help in that only.

Currently these scripts are only for programming in C++ (If you want to extend to others, modifying the scripts is quite easy).

Installation and Configuration
------------------------------
1. Download this repository.
2. Navigate to repository and give permission to files for execution
```bash
chmod +x gen.sh
chmod +x scripts/ver.sh
chmod +x scripts/run.sh
```
3. __Before creating folder for any contest__, each time navigate to main repository and excute following commands in given sequence
```bash
alias gen=./gen.sh
cd scripts
alias ver=./ver.sh
alias run=./run.sh
```
4. Update the template.cpp file as needed. It's content will be initial content of each .cpp file created further.

How to Use
----------
Suppose you want to participate or want to solve problems in http://codeforces.com/contest/1155

* Navigate to main directory and run 'gen' command.
* Enter Contest ID (say 1155 for this contest).
* If contest is not started yet, program will terminate.
* If started, it will create folder "cf_"contest_id (say cf_1155) containing empty test case folder and ver.sh script.
* Now, script will import problem list and test cases.
* Finally, we will have a folder with .cpp files, one for each problem along with Test case folder where all imported test cases will be placed.
* Now, navigate to contest folder by 'cd cf_1155' command.
* Write the solution for a problem (say D) in respective file (d.cpp).
* Run 'ver d' or 'ver D' to test your solution d.cpp with sample test cases for problem D imported from website.
* To test your solution d.cpp with custom test case, run 'run' command and get output by entering respective arguments. __Custom input arguments should be placed in a single line__.
* If you get any error related to 'run', 'ver' or 'run' commands, refer to point 3 in 'Installation and Configuration'.
