#!/bin/bash

set -e

for i in *.fa
do
srun -N1 -c250 ~/bin/bowtie-build --threads 250 -o 2 $i ${i::-3}
done


for i in *.fa
do

srun -N1 -c250 ~/bin/bowtie -v 0 -y --norc -a -p 250 -f ../u36.fa -x ${i::-3} -S u36_on_${i::-3}.sam
srun -N1 -c250 ~/bin/bowtie -v 0 -y --norc -a -p 250 -f ../o35.fa -x ${i::-3} -S o35_on_${i::-3}.sam

samtools view -F 4 u36_on_${i::-3}.sam -o u36_on_${i::-3}m.sam
samtools view -F 4 o35_on_${i::-3}.sam -o o35_on_${i::-3}m.sam

rm u36_on_${i::-3}.sam
rm o35_on_${i::-3}.sam

cut -f4 u36_on_${i::-3}m.sam > u36_on_${i::-3}m.f4
cut -f4 o35_on_${i::-3}m.sam > o35_on_${i::-3}m.f4
cat u36_on_${i::-3}m.f4 o35_on_${i::-3}m.f4 > u257_on_${i::-3}m.f4

rm u36_on_${i::-3}m.sam
rm o35_on_${i::-3}m.sam

python ft.py u36_on_${i::-3}m.f4 300 300 1,2,5,10,15,20,25,30,50
python ft.py o35_on_${i::-3}m.f4 300 300 1,2,5,10,15,20,25,30,50
python ft.py u257_on_${i::-3}m.f4 300 300 1,2,5,10,15,20,25,30,50

done
