#!/bin/bash

echo "Tech_Node,Access_Time(ns),Read_Energy(nJ),Area(mm2)" > results_tech.csv

# The list of nodes we simulated
techs=("90nm" "65nm" "45nm" "32nm" "22nm")

for tech in "${techs[@]}"; do
    file="runs/tech_${tech}.txt"
    
    # Extract Data
    time=$(grep "Access time (ns)" $file | awk '{print $4}')
    energy=$(grep "Total dynamic read energy" $file | awk '{print $8}')
    area=$(grep -m 1 "Data array: Area" $file | awk '{print $5}')
    
    echo "$tech,$time,$energy,$area" >> results_tech.csv
done

echo "Extraction Complete. Check results_tech.csv"