Auto Test Case Checker
=====================
http://codeforces.com conducts programming contests. While participating in the contest, it would be better if we could check all the sample test cases by running a single command. These scripts help exactly there.

Currently these scripts are only for programming in C++ (If you want to extend to others, modifying the scripts should be easy).

Installation and Configuration
------------------------------
* Download this repository.
* Update the template.cpp file as needed.

Usage
-----
Suppose you want to participate in http://codeforces.com/contest/1155

Note the number at the end, 1155, which we shall be using in the following commands.

* Run './gen.sh'
* It will ask you contest ID, number of problems and test case import flag value. For this contest, Contest ID is 1155 and number of problems is 6.
* By doing this you are creating folder with those many .cpp files and test case folder.
* **If you are creating folder before the contest**, number of problems will be specified in the respective blog of contest. Also, contest ID can be seen in URL by clicking on contest registrants list link https://codeforces.com/contestRegistrants/1155 (list of people registered for contest, it is always present in rightmost column in contests lists https://codeforces.com/contests).
* Test Case import Flag is either 0 or 1. Flag is to be kept 0 if you are creating folder before contest as test cases will not be available then. Flag is to be kept 1 if contest is started and problems are released.
* This creates a folder named 1155, with a .cpp file for each problem whose content is the same as the template.cpp file which you have configured.
* cd 1155
* Write the code for a problem (say D)
* Run './ver.sh d' or './ver.sh D' to verify Problem : D with sample test cases provided in the website.
