#!/bin/bash
read -p "Enter Contest ID : " id
if [[ -z "$id" || -n ${id//[0-9]/} ]];then
	echo "Please enter valid integer ID"
	exit 1
fi

pyth=""
if command -v python3 &>/dev/null; then
	pyth="python3"
else
	echo "Requirement python3 not satisfied"
	exit 1
fi

echo "Processing ..."
problems=$(${pyth} static/problem_list_import.py $id)
if [[ "$?" -eq 0 ]];then
	echo "Invalid Contest ID/ Problems are not released yet/ Network Error"
	exit 1
fi

read -p "Enter problem IDs (to import all problems, just press ENTER) : " task_id
task_id=$(echo $task_id | awk '{print toupper($0)}')
echo "Processing ..."
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

mkdir -p contests/"cf_"$id
mkdir -p contests/"cf_"$id/test_cases/
mkdir -p contests/"cf_"$id/ps/
cd contests
cd "cf_"$id
ln -fs ../../static/ver.sh ver.sh
ln -fs ../../static/run.sh run.sh
cd ..
cd ..

declare -a problem_list
for i in $problems;
do
	problem_list+=($i)
done

${pyth} update_contest.py $id $problems
problem_count=${#problem_list[@]}

read -p "Do you want to overwrite .cpp files(if exists) [y/n] : " cpp_overwrite

for problem in ${problem_list[@]};
do
	if [ -f contests/"cf_"$id/$problem".cpp" ];then
		if [[ "$cpp_overwrite" == "n" ]];then
			echo $problem" -> "$problem".cpp already exists"
		else
			cp -n --no-clobber template.cpp contests/"cf_"$id/$problem.cpp
			echo $problem" -> "$problem".cpp overwritten"
		fi
	else
		cp -n --no-clobber template.cpp contests/"cf_"$id/$problem.cpp
		echo $problem" -> "$problem".cpp created"
	fi
done

echo -n "Test Case and Problem Statement Fetching : "

c=0
d=0
for problem in ${problem_list[@]};
do
	echo -n $problem" "
	${pyth} static/test_case_import.py $id $problem
	c=$(( $c + $? ))
	${pyth} static/ps_import.py $id $problem
	d=$(( $d + $? ))
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

if [[ "$d" -eq "${problem_count}" ]];then
	echo "Problem Statements Downloaded :)"
else
	echo "Problem Statements downloading failed :("
	echo "Please Try again"
fi