# Permute nucleotides in CSV file back to original data
# by changing A's to T's and T's to A's
# Usage: bash permute_nucleotides.sh > output_file

# first temporarily substitute X for A,
# then swith T to A, then switch X to T.
gsed -e 's/A/X/g' -e 's/T/A/g' -e 's/X/T/g' data/raw/tableofSNPs.csv
