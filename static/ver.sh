#!/bin/bash
taskid=$(echo $1 | awk '{print toupper($0)}')
if [ -f $taskid".cpp" ];then
	echo -n ""
elif [[ -z "$taskid" ]];then
	echo "Please mention problem ID (e.g. 'run D' )"
	exit 1
else
	echo $taskid".cpp does not exists"
	exit 1
fi

g++ $taskid.cpp -D ONLINE_JUDGE
if [ $? -eq 0 ];then
	echo "Compiling "$taskid".cpp successful !"
	echo "-----------------------------------"
	if [ -f "test_cases/"$taskid"_num_samples" ];then
		echo -n ""
	else
		echo "Test cases are not available/imported"
		exit 1
	fi
	numsamples=$(cat test_cases\/${taskid}_num_samples)
	for test_id_ in $(seq 1 ${numsamples})
	do
		test_id=$(echo ${test_id_} - 1 |bc)
		./a.out < test_cases/$taskid"_in_"$test_id > test_cases/$taskid"_myout_"$test_id
		diff_data=$(diff test_cases/${taskid}"_myout_"$test_id test_cases/$taskid"_out_"$test_id -bB)
		echo -n "Test case #"$test_id" : "
		tab="    "
		if [ "$diff_data" == "" ];then
			echo "PASSED"
			echo "$tab|--------------------------------"
			echo "$tab| Output : "
			awk -v tab="${tab}" '{print tab"| " $0 }' test_cases/$taskid"_out_"$test_id
			echo "$tab|--------------------------------"
		else
			echo "FAILED"
			echo "$tab|--------------------------------"
			echo "$tab| Expected output : "
			awk  -v tab="${tab}" '{ print tab"| " $0 }'  test_cases/$taskid"_out_"$test_id
			echo "$tab|--------------------------------"
			echo "$tab| Your output : "
			awk  -v tab="${tab}" '{ print tab"| " $0 }'  test_cases/$taskid"_myout_"$test_id
			echo "$tab|--------------------------------"
		fi
	done
else
   echo "==============================="
   echo "Compiling "$taskid".cpp FAILED!"
fi
