#!/bin/bash
opers='seqwr rndrw'
dir=$(pwd)

target=$dir/qemu_fileio_test_res.txt
if [ ! -f $target ]
then
	touch $target
	echo "QEMU cput test result" >> $target
fi

for oper in $opers;
do	
	echo "max prime $prime" >> $target
	for i in 1 2 3 4 5;
	do
	echo "iteration $i" >> $target
	sysbench --num-threads=16 --test=fileio --file-total-size=3G --file-test-mode=$oper prepare
	sysbench --num-threads=16 --test=fileio --file-total-size=3G --file-test-mode=$oper run >> $target
	sysbench --num-threads=16 --test=fileio --file-total-size=3G --file-test-mode=$oper cleanup
	done
done 
