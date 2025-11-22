#!/bin/bash

# 1. Write the Header Row for the CSV file
echo "Size,Associativity,Access_Time(ns),Read_Energy(nJ),Area(mm2)" > results.csv

# Define the labels to look for
sizes=("16KB" "32KB" "64KB" "128KB" "256KB" "512KB" "1MB" "2MB")
assocs=(2 4 8 16)

# Loop through all files
for sz in "${sizes[@]}"; do
    for asc in "${assocs[@]}"; do
        
        file="runs/${sz}_assoc_${asc}.txt"
        
        # Extract the numbers using grep and awk
        # $4 means "take the 4th word" (the number)
        time=$(grep "Access time (ns)" $file | awk '{print $4}')
        
        # $8 means "take the 8th word"
        energy=$(grep "Total dynamic read energy" $file | awk '{print $8}')
        
        # $5 means "take the 5th word"
        area=$(grep -m 1 "Data array: Area" $file | awk '{print $5}')
        
        # Append to the CSV file
        echo "$sz,$asc,$time,$energy,$area" >> results.csv
    done
done

echo "Extraction Complete! Open 'results.csv' to see your data."