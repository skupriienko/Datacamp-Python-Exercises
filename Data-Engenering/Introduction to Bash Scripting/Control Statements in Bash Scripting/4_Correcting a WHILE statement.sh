#!/usr/bash

emp_num=1
while [ $emp_num -le 1000 ];
do
    cat "$emp_num-dailySales.txt"|egrep'Sales_total'|sed 's/.* ://' > "$emp_num-agg.txt"
done
