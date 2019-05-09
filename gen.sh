#!/bin/bash
read -p "Enter Contest ID, problem count and Test Case import Flag : " id c f
mkdir -p "cf_"$id
mkdir -p "cf_"$id/test_cases/
cd "cf_"$id
ln -fs ../scripts/ver.sh ver.sh
cd ..

problem_count=$c
test_import_flag=$f
for problem_num in $(seq 1 ${problem_count})
do
	problem_num=$(echo $problem_num+96 | bc)
	problem=$(printf "\x$(printf %x $problem_num)")
	echo $problem" -> "$problem".cpp created "
	if [ -f "cf_"$id/$problem.cpp ];then
		rm "cf_"$id/$problem.cpp
	fi
	cp -n --no-clobber template.cpp "cf_"$id/$problem.cpp
done

if [[ "$test_import_flag" == 1 ]];then
	wget -q --spider "http://codeforces.com/contest/"$id
	if [[ $? -ne 0 ]];then
		echo "No Internet Connetion"
		exit 1
	fi

	pyth=""
	if command -v python3 &>/dev/null; then
		pyth="python3"
	elif command -v python &>/dev/null; then
		pyth="python"
	else
		echo "Requirement python or python3 not satisfied"
		exit 1
	fi 

	while [ 1 ];
	do
		echo -n "Test Case Fetching ... "
		c=0
		for problem_num in $(seq 1 ${problem_count})
		do
			problem_num=$(echo $problem_num+96 | bc)
			problem=$(printf "\x$(printf %x $problem_num)")
			echo -n $problem" "
			${pyth} scripts/test_case_import.py $id $problem
			c=$(( $c + $?))
		done
		if [[ "$c" -eq "${problem_count}" ]];then
			echo $'\n'"Test Case Fetching Complete !"
			break
		else
			echo $'\n'
		fi
	done
fi