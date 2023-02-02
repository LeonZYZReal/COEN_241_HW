#!/bin/bash
threads='2 4 6'
dir=$(pwd)

target=$dir/docker_cpu_test_res.txt
if [ ! -f $target ]
then
	touch $target
	echo "QEMU cput test result" >> $target
fi

for thread in $threads;
do	
	echo "max prime $prime" >> $target
	for i in 1 2 3 4 5;
	do
	echo "iteration $i" >> $target
	sysbench --test=cpu --num-threads=$thread --cpu-max-prime=20000 --max-time=30 run >> $target
	done
done 
