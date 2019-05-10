#!/bin/bash
read -p "Enter Contest ID : " id
mkdir -p "cf_"$id
mkdir -p "cf_"$id/test_cases/
cd "cf_"$id
ln -fs ../scripts/ver.sh ver.sh
cd ..

pyth=""
if command -v python3 &>/dev/null;then
	pyth="python3"
elif command -v python &>/dev/null; then
	pyth="python"
else
	echo "Requirement python or python3 not satisfied"
	exit 1
fi

f=1
while [ 1 ];
do
	if [[ "$f" -eq "6" ]];then
		echo $'\n'"5 Tries completed. Terminating Program ... "
		break
	fi
	echo "Try "$f" : "
	f=$(( $f + 1 ))

	problems=$(${pyth} scripts/problem_list_import.py $id)

	if [[ "$?" -eq 0 ]];then
		echo "Problems are not released yet"
		continue
	fi

	declare -a problem_list
	for i in $problems;
	do
		problem_list+=($i)
	done
	problem_count=${#problem_list[@]}

	for problem in ${problem_list[@]};
	do
		if [ -f "cf_"$id/$problem".cpp" ];then
			echo $problem" -> "$problem".cpp already exists"
		else
			echo $problem" -> "$problem".cpp created"
			cp -n --no-clobber template.cpp "cf_"$id/$problem.cpp
		fi
	done

	echo -n "Test Case Fetching : "
	c=0
	for problem in ${problem_list[@]};
	do
		echo -n $problem" "
		${pyth} scripts/test_case_import.py $id $problem
		c=$(( $c + $? ))
	done
	if [[ "$c" -eq "${problem_count}" ]];then
		echo $'\n'"Test Case Fetching Complete :)"
		break
	elif [[ "$c" -ne 0 ]];then
		echo $'\n'"Partial Test Case Fetching Done !"
	else
		echo $'\n'"Test Case Fetching Failed :("
	fi
done