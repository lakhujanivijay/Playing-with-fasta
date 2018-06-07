#shell wrapper around seqkit to calculate length distribution of fasta sequences

# Usage 
# [cmd_prompt]$ source length_dist.sh <fasta_file.fa>

# Requires
# seqkit: https://bioinf.shenwei.me/seqkit/

echo -ne "Length < 200:\t"
cat $1 |  seqkit seq -M 199 | seqkit stat -T | grep -v file | cut -f 4

echo -ne "Length >= 200 && <= 300:\t"
cat $1 |  seqkit seq -m 200 -M 300 | seqkit stat -T | grep -v file | cut -f 4

for i in $(seq 300 100 900); do 
  echo -ne "Length > $i && <= $(expr $i + 100):\t" 
  cat $1 |  seqkit seq -m $(expr $i + 1) -M $(expr $i + 100) | seqkit stat -T | grep -v file | cut -f 4
done

echo -ne "Length > 1000 && <=5000:\t"
cat $1 |  seqkit seq -m 1001 -M 5000 | seqkit stat -T | grep -v file | cut -f 4

echo -ne "Length >5000:\t" 
cat $1 |  seqkit seq -m 5000 | seqkit stat -T | grep -v file | cut -f 4
