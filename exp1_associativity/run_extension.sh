#!/bin/bash

# Define ONLY the new Large Sizes (4MB to 32MB)
# 4MB, 8MB, 16MB, 32MB
sizes=(4194304 8388608 16777216 33554432)
size_labels=("4MB" "8MB" "16MB" "32MB")

# Define associativities
assocs=(2 4 8 16)

# Path to the CACTI tool (It is one level up)
CACTI_TOOL="../cacti"

# Loop
for ((i=0; i<${#sizes[@]}; i++)); do
    curr_size=${sizes[$i]}
    curr_label=${size_labels[$i]}

    for curr_assoc in "${assocs[@]}"; do
        
        # Define file names
        cfg_name="configs/${curr_label}_assoc_${curr_assoc}.cfg"
        out_name="runs/${curr_label}_assoc_${curr_assoc}.txt"

        # 1. Create config from baseline
        cp configs/baseline.cfg $cfg_name

        # 2. Modify SIZE
        sed -i "s/-size (bytes) 32768/-size (bytes) $curr_size/" $cfg_name

        # 3. Modify ASSOCIATIVITY
        sed -i "s/-associativity 8/-associativity $curr_assoc/" $cfg_name

        # 4. Run CACTI
        echo "Running: Size $curr_label | Assoc $curr_assoc ..."
        (cd .. && ./cacti -infile exp1_associativity/$cfg_name > exp1_associativity/$out_name)

    done
done

echo "Extension Simulations Complete!"