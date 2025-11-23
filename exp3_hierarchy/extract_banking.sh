#!/bin/bash

echo "Banks,Access_Time(ns),Cycle_Time(ns),Area(mm2)" > results_banking.csv

banks=(1 2 4 8 16 32 64)

for b in "${banks[@]}"; do
    file="runs_banking/L3_8MB_banks_${b}.txt"
    
    # Extract Data
    acc=$(grep "Access time (ns)" $file | awk '{print $4}')
    cyc=$(grep "Cycle time (ns)" $file | awk '{print $4}')
    area=$(grep -m 1 "Data array: Area" $file | awk '{print $5}')
    
    echo "$b,$acc,$cyc,$area" >> results_banking.csv
done

echo "Data Extracted."