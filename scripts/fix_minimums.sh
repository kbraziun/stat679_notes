# Fix minimum column in CSV file to remove quotations and commas
# in numeric column
# Usage: bash fix_minimum.sh > output_file

# find all numbers that are surrounded by quotes
# and remove both the quotations and the commas.
# works for numbers in the thousands or millions
gsed -E 's/"([0-9]+),([0-9]*),*([0-9]+)"/\1\2\3/g' data/raw/tableofSNPs.csv
