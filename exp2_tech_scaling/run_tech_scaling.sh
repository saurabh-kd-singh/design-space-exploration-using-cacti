#!/bin/bash

# Define Technology Nodes (microns)
# 90nm, 65nm, 45nm, 32nm, 22nm
techs=(0.090 0.065 0.045 0.032 0.022)
labels=("90nm" "65nm" "45nm" "32nm" "22nm")

# Path to CACTI (one level up)
CACTI_TOOL="../cacti"

# Loop through nodes
for ((i=0; i<${#techs[@]}; i++)); do
    curr_tech=${techs[$i]}
    curr_label=${labels[$i]}
    
    # Files
    cfg_name="configs/tech_${curr_label}.cfg"
    out_name="runs/tech_${curr_label}.txt"
    
    # 1. Create config from baseline
    cp configs/baseline.cfg $cfg_name
    
    # 2. Modify TECHNOLOGY NODE
    # We look for "-technology (u) 0.022" and replace it
    sed -i "s/-technology (u) 0.022/-technology (u) $curr_tech/" $cfg_name
    
    # 3. Run CACTI
    echo "Simulating Node: $curr_label ($curr_tech u)..."
    (cd .. && ./cacti -infile exp2_tech_scaling/$cfg_name > exp2_tech_scaling/$out_name)
    
done

echo "Moore's Law Simulation Complete!"