Auto Test Case Checker (ATCC)
=====================

http://codeforces.com conducts programming contests. While participating in the contest or upsolving, it would be better if we could check all the sample test cases by running a single script. Also, we may need to solve problems without internet connection and check solutions on sample test cases. This repository is going to help in that only.

Currently these scripts are only for programming in C++ (To extend it to others, modifying the scripts is quite easy).

Installation and Configuration
------------------------------
1. Download/clone this repository.
2. To install dependencies, refer to [requirements.txt](./requirements.txt)
3. Navigate to repository and run following commands in given sequence :
```bash
cd static
git clone https://github.com/mathjax/MathJax.git ./MathJax
cd ..
python3 db_setup.py
source init.sh
```
4. Update the template.cpp file as needed. It's content will be initial content of each .cpp file created further.
5. Place your USERNAME and PASSWORD in [credentials.py](static/credentials.py) file in static folder.

How to Use
----------
Suppose you want to participate or to solve problems in http://codeforces.com/contest/1163

* Navigate to repository. Run the server by running __python3 main.py__ command. Server will be running at http://127.0.0.1:5000/ 
* Open another terminal and run __source init.sh__ command. It gives permissions to .sh files for execution and initializes __sol__, __ver__ and __run__ commands. __Every time you open new terminal, you need to execute this command to use sol, ver and run commands__.
* Then, run __sol__ command. Enter Contest ID (say 1163 for this contest). Enter __space-separated__ problem IDs for problems you want to solve (say A B1 B2). __If you want to solve all problems, keep this place blank and just press ENTER__.
* If any error occurs(invalid contest ID, network error or if problems are not released), program will terminate.
* If already released, it will create a folder "cf_"contest_id (say cf_1163) containing .cpp files, one for each problem along with scripts (ver.sh and run.sh), Test case folder where all imported test cases will be placed and ps folder where all imported __html__ problem statements will be placed.
* Now, go to server and navigate to problem you want to solve. Also, navigate to contest folder by __cd cf_1163__ command in terminal. Write the solution for a problem (say D) in respective file (D.cpp).
* Run __ver d__ or __ver D__ to test your solution D.cpp with imported sample test cases for problem D.
* To test your solution D.cpp with custom test case, run __run d__ or __run D__ command and get output by entering respective custom input. __Whole custom input should be entered in a single line__.
* If all sample test cases are passed and want to submit the file, click "SUBMIT CODE" button and wait for final confirmation. __Do not reload or close tab after submitting the code(after clicking SUBMIT CODE) until final confirmation(Solution Submitted) occurs__.

Note
----
* It is allowed to call __sol__ any number of times for a single contest. Everytime, test cases and problem statements will be created/updated for respective problems. __.cpp files will be overwritten only if user permits to do so__.
* It is possible that due to bad network or some other reason, program may terminate throwing an error or take longer than expected. That time, it is adviced to terminate the program( ctrl + z ) and try again with same procedure followed before.
* Tags present in problem statements are updated only when they are imported again using __sol__ command.
* In problem statement, if any unknown mathematical symbols(specially latex syntex) are seen, refresh the tab so that MathJax will be loaded properly.
* If you want to erase all contests from Database or want to erase all contest cf_* repositories, run __python3 db_setup.py__ command.
