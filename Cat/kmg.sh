#!/bin/bash

set -e

echo "Prefix: $1" 

echo "fa entries:"
grep -c '>' ${1}.fa

seqtk seq -F '5' ${1}.fa > ${1}.fq

echo "fq entries:"
echo $(wc -l i1c.fq | cut -d' ' -f1)/4|bc

mkdir kmcc
cd kmcc

mkdir k_t

for i in {4..256}
do 
kmc -k$i -m300 -fq -ci10 -cs999999999 -t80 ../$1.fq k$i k_t
kmc_tools transform k$i dump k$i.txt
done

cat k{4..256}.txt > ../k.xt 

cd ../
rm -r kmcc

mkdir kmfa
python wgkm.py k.xt 

cat kmfa/{4..35}.fa > u36.fa
cat kmfa/{36..256}.fa > o35.fa
