#!/bin/bash

# Write Header
echo "Tech,Type,Latency(ns),Leakage_Power(mW),Area(mm2)" > results_comparison.csv

techs=("90nm" "65nm" "45nm" "32nm" "22nm")
types=("HP" "LSTP")

for tech in "${techs[@]}"; do
    for type in "${types[@]}"; do
        
        file="runs/tech_${tech}_type_${type}.txt"
        
        # 1. Extract Latency (4th word)
        lat=$(grep "Access time (ns)" $file | awk '{print $4}')
        
        # 2. Extract TOTAL LEAKAGE (Corrected)
        # We look for "Total leakage power of a bank" and take the 8th word
        # We use -m 1 to ensure we only grab the first (main) line, not the sub-banks
        leak=$(grep -m 1 "Total leakage power of a bank (mW):" $file | awk '{print $8}')
        
        # 3. Extract Area (5th word)
        area=$(grep -m 1 "Data array: Area" $file | awk '{print $5}')
        
        echo "$tech,$type,$lat,$leak,$area" >> results_comparison.csv
    done
done

echo "Extraction Complete. Check results_comparison.csv"