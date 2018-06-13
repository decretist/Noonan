#!/bin/bash
#
# Paul Evans (pevans@sandiego.edu)
# 13 June 2018
#
export AUTO="$HOME/Work/Gratian/samples/auto/1r"
export HAND="$HOME/Work/Gratian/samples/hand/1r"
export CASES="$HOME/Work/Gratian/samples/hand/cases"
#
cp -i -p $HAND/C\.2[789]* .
cp -i -p $HAND/C\.3[0123456]* .
cp -i -p $HAND/de\ Pen* .
#
for file in *.txt
do
# echo $file
diff "$file" $AUTO/"$file"
# echo $?
done
#
for file in *.txt
do
# echo $file
diff "$file" $HAND/"$file"
# echo $?
done
#
cp -i -p $CASES/*d\.init* .
#
for file in *d\.init.txt
do
# echo $file
diff "$file" $CASES/"$file"
# echo $?
done

