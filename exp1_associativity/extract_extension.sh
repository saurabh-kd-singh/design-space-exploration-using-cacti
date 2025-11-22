#!/bin/bash

# Define only the NEW labels
sizes=("4MB" "8MB" "16MB" "32MB")
assocs=(2 4 8 16)

# Loop through files and APPEND to final_results.csv
for sz in "${sizes[@]}"; do
    for asc in "${assocs[@]}"; do
        
        file="runs/${sz}_assoc_${asc}.txt"
        
        # Extract the numbers
        time=$(grep "Access time (ns)" $file | awk '{print $4}')
        energy=$(grep "Total dynamic read energy" $file | awk '{print $8}')
        area=$(grep -m 1 "Data array: Area" $file | awk '{print $5}')
        
        # Check if data exists (to avoid empty lines if a run failed)
        if [ ! -z "$time" ]; then
            echo "$sz,$asc,$time,$energy,$area" >> final_results.csv
            echo "Added $sz / $asc to CSV."
        else
            echo "Skipping $sz / $asc (No data found)"
        fi
    done
done

echo "Data Append Complete! Open final_results.csv to check."