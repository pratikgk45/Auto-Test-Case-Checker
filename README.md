Auto Test Case Checker (ATCC)
=====================

__TO BE UPDATED__

http://codeforces.com conducts programming contests. While participating in the contest or upsolving, it would be better if we could check all the sample test cases by running a single script. Also, we may need to solve problems without internet connection and check solutions on sample test cases. This repository is going to help in that only.

Currently these scripts are only for programming in C++ (If you want to extend to others, modifying the scripts is quite easy).

Installation and Configuration
------------------------------
1. Download/clone this repository.
2. To install dependencies, refer to [requirements.txt](./requirements.txt)
3. Navigate to repository and run following commands in given sequence :
```bash
cd scripts
mkdir MathJax-2.7.3
git clone https://github.com/mathjax/MathJax.git ./MathJax-2.7.3/
cd ..
python3 db_setup.py
source init.sh
```
4. Update the template.cpp file as needed. It's content will be initial content of each .cpp file created further.
5. Place your username and password in credentials.py file in static folder.

How to Use
----------
Suppose you want to participate or to solve problems in http://codeforces.com/contest/1163

* Navigate to repository. Run __source init.sh__ command.
* Then, run __sol__ command. Enter Contest ID (say 1163 for this contest). Enter __space-separated__ problem IDs for problems you want to solve (say A B1 B2). __If you want to solve all problems, keep this place blank and just press ENTER__.
* If any error occurs(invalid contest ID, network error or if problems are not released yet), program will terminate.
* If already released, it will create a folder "cf_"contest_id (say cf_1163) containing .cpp files, one for each problem along with scripts (ver.sh and run.sh), Test case folder where all imported test cases will be placed and ps folder where all imported __html__ problem statements will be placed.
* If you want to see/solve problems __offline__, problem statements will be available in __ps__ folder in "cf_"contest_id folder.
* Now, navigate to contest folder by __cd cf_1163__ command.
* Write the solution for a problem (say D) in respective file (D.cpp).
* Run __ver d__ or __ver D__ to test your solution D.cpp with imported sample test cases for problem D.
* To test your solution D.cpp with custom test case, run __run d__ or __run D__ command and get output by entering respective custom input. __Whole custom input should be entered on a single line__.
* If you get any error related to __sol__, __ver__ or __run__ commands or about permission, refer to point 2 in 'Installation and Configuration' section.

Note
----
* It is allowed to call __sol__ any number of times for a single contest. Everytime, test cases and problem statements will be created/updated for respective problems. __.cpp files will be overwritten only if user permits to do so__.
* It is possible that due to bad network or some other reason, program may terminate throwing an error or take longer than expected. That time, it is adviced to terminate the program( ctrl + z ) and try again with same procedure followed before.
* Tags present in problem statements are updated only when they are imported again using __sol__ command.
* In problem statement, if any unknown mathematical symbols(specially latex syntex) are seen, refresh the tab so that MathJax will be loaded properly.
* __Do not reload or close tab after submitting the code(after clicking SUBMIT CODE) until final confirmation(Solution Submitted) occurs__.
* If you want to erase all contests from Database or want to erase all contest cf_* repositories, run __python3 db_setup.py__ command.