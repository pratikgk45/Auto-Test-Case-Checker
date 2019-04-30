#!/bin/bash
read -p "Contest ID, problem count and Test Case import Flag : " id c f
mkdir -p $id
mkdir -p $id/tests/
cd $id
ln -fs ../scripts/ver.sh ver.sh
cd ..

problem_count=$c
test_import=$f
echo $problem_count
echo $test_import
for problem_num in $(seq 1 ${problem_count})
do
	problem_num=$(echo $problem_num+96 | bc)
	problem=$(printf "\x$(printf %x $problem_num)")
	echo -n $problem" "
	cp -n --no-clobber template.cpp $id/$problem.cpp
	if [[ "$test_import" == 1 ]];then
		python scripts/generate_problem.py $id $problem
	fi
done
