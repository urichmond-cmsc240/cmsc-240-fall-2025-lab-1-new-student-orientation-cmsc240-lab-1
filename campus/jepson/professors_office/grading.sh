python_file=$1
name=$(echo $python_file | sed 's/\[\(.*\)\].*/\1/')
output="_${name}-p1-out.txt"
script -q -a $output python $python_file 
cat $output | col -bp > "_${name}-p1-out2.txt"
rm $output
mv "_${name}-p1-out2.txt" $output