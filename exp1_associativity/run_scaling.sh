#!/bin/bash

# Define sizes (16KB to 2MB)
sizes=(16384 32768 65536 131072 262144 524288 1048576 2097152)
size_labels=("16KB" "32KB" "64KB" "128KB" "256KB" "512KB" "1MB" "2MB")

# Define associativities
assocs=(2 4 8 16)

# Path to the CACTI tool (It is one level up)
CACTI_TOOL="../cacti"

# Loop
for ((i=0; i<${#sizes[@]}; i++)); do
    curr_size=${sizes[$i]}
    curr_label=${size_labels[$i]}

    for curr_assoc in "${assocs[@]}"; do
        
        # --- SKIP LOGIC ---
        # If size is 16KB and Associativity is 16, skip this iteration
        if [ "$curr_label" == "16KB" ] && [ "$curr_assoc" -eq 16 ]; then
            echo "Skipping invalid combination: 16KB with 16-way..."
            continue
        fi
        # ------------------

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

echo "All Simulations Complete (Skipped 16KB/16-way)!"