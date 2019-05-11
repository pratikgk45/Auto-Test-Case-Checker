#!/bin/bash
read -p "Enter Contest ID : " id
if [[ -z "$id" || -n ${id//[0-9]/} ]];then
	echo "Please enter valid integer ID"
	exit 1
fi

pyth=""
if command -v python3 &>/dev/null;then
	pyth="python3"
elif command -v python &>/dev/null; then
	pyth="python"
else
	echo "Requirement python or python3 not satisfied"
	exit 1
fi

read -p "Enter problem IDs (to import all problems from contest, keep it empty) : " task_id
problems=$(${pyth} scripts/problem_list_import.py $id)
if [[ "$?" -eq 0 ]];then
	echo "Problems are not released yet"
	exit 1
fi
if [[ ! -z "$task_id" ]];then
	c=0
	d=0
	for i in $task_id;
	do
		d=$(( $d + 1 ))
		for j in $problems;
		do
			if [[ "$i" == "$j" ]];then
				c=$(( $c + 1 ))
				break
			fi
		done
	done
	if [[ "$c" -ne "$d" ]];then
		echo "Please enter valid problem IDs"
		exit 1
	fi
	problems=$task_id
fi

mkdir -p "cf_"$id
mkdir -p "cf_"$id/test_cases/
cd "cf_"$id
ln -fs ../scripts/ver.sh ver.sh
ln -fs ../scripts/run.sh run.sh
cd ..

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
elif [[ "$c" -ne 0 ]];then
	echo $'\n'"Partial Test Case Fetching Done !"
	echo "Please Try again"
else
	echo $'\n'"Test Case Fetching Failed :("
	echo "Please Try again"
fi