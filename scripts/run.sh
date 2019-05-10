#!/bin/bash
taskid=$(echo $1 | awk '{print toupper($0)}')
if [ -f $taskid".cpp" ];then
	echo -n ""
elif [[ -z "$taskid" ]];then
	echo "Please mention problem ID"
	exit 1
else
	echo $taskid".cpp does not exists"
	exit 1
fi
g++ $taskid.cpp -D ONLINE_JUDGE
if [ $? -eq 0 ];then
	echo "Compiling "$taskid".cpp successful !"
	echo "-----------------------------------"
	tab="    "
	read -p "$tab| Enter input arguments : " input
	echo $input > temp_in
	./a.out < temp_in > temp_out
	echo "$tab|--------------------------------"
	echo "$tab| Output : "
	awk -v tab="${tab}" '{print tab"| " $0 }' temp_out
	echo "$tab|--------------------------------"
else
   echo "==============================="
   echo "Compiling "$taskid".cpp FAILED!"
fi
