# Create variable from first ARGV element
sfile=$1

# Create an IF statement on first ARGV element's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile; then
    # Move file if matched
    mv $sfile good_logs/
fi
