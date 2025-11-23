#!/bin/bash

# Define the 3 levels
levels=("L1_fast" "L2_balanced" "L3_huge")

# Create runs folder if it doesn't exist
mkdir -p runs

# Run Loop
for lvl in "${levels[@]}"; do
    echo "Simulating $lvl..."
    
    # EXPLANATION:
    # We use (cd .. && ...) to temporarily jump up to the main folder 
    # so CACTI can find its system files, then we point it back down 
    # to this folder for the inputs and outputs.
    (cd .. && ./cacti -infile exp3_hierarchy/configs/${lvl}.cfg > exp3_hierarchy/runs/${lvl}.txt)
done

echo "Hierarchy Simulations Complete!"