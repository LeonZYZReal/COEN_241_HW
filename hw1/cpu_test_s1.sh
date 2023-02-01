#!/bin/bash
primes='20000 40000 60000'
dir=$(pwd)

target=$dir/qemu_cpu_test_res.txt
if [ ! -f $target ]
then
	touch $target
	echo "QEMU cput test result" >> $target
fi

for prime in $primes;
do	
	echo "max prime $prime" >> $target
	for i in {1..5}
	do
	echo "iteration $i" >> $target
	sysbench --test=cpu --cpu-max-prime=$prime --max-time=30 run >> $target
	done
done 
