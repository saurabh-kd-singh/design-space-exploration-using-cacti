#!/bin/bash

# Write Header
echo "Level,Latency(ns),Read_Energy(nJ),Leakage_Power(mW),Area(mm2)" > results_hierarchy.csv

levels=("L1_fast" "L2_balanced" "L3_huge")

for lvl in "${levels[@]}"; do
    file="runs/${lvl}.txt"
    
    # 1. Latency
    lat=$(grep "Access time (ns)" $file | awk '{print $4}')
    
    # 2. Dynamic Energy
    dyn=$(grep "Total dynamic read energy" $file | awk '{print $8}')
    
    # 3. Leakage Power (Using the pattern we found in Exp 2)
    # "Total leakage power of a bank (mW): 12.345" -> 8th word
    leak=$(grep -m 1 "Total leakage power of a bank (mW):" $file | awk '{print $8}')
    
    # 4. Area
    area=$(grep -m 1 "Data array: Area" $file | awk '{print $5}')
    
    echo "$lvl,$lat,$dyn,$leak,$area" >> results_hierarchy.csv
done

echo "Hierarchy Data Extracted. Check results_hierarchy.csv"