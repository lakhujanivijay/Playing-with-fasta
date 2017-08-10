#!/usr/bin/python2.7
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"
__date__= "09 Aug 2017"


from Bio import SeqIO
import getopt, sys

count=0

def usage():
    print "Usage: per_sequence_coverage.py -i <input_fasta.fa>"


try:
    options, remainder=getopt.getopt(sys.argv[1:], 'i:h')

except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit()

for opt, arg in options:
    if opt in ('-i'):
        input_file=arg
    if opt in ('-h'):
        usage()
	sys.exit()

try:
    file = open(input_file)
 
except IOError:
    print "fasta file cannot be opened"

print "Sequence_ID\tSequence_Length\tTotal_gaps\tPercent_coverage"

for record in SeqIO.parse(file, "fasta"):
    seq_len=len(record.seq)
    N_count=str(record.seq).count("N")
    n_count=str(record.seq).count("n")
    total_gaps= N_count + n_count
    consensus_len=seq_len - total_gaps
    percent_coverage=round((float(consensus_len)/float(seq_len)) * 100 , 2)
    print record.description + "\t" + str(len(record.seq)) + "\t" + str(total_gaps) + "\t" + str(percent_coverage)
file.close()
