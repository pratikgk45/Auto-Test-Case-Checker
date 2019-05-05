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
	echo -n $problem" "
	cp -n --no-clobber template.cpp "cf_"$id/$problem.cpp
	if [[ "$test_import_flag" == 1 ]];then
		python scripts/generate_problem.py $id $problem
	fi
done
