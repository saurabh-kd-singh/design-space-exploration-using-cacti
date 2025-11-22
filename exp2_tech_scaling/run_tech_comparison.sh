#!/bin/bash

# Define Nodes
techs=(0.090 0.065 0.045 0.032 0.022)
tech_labels=("90nm" "65nm" "45nm" "32nm" "22nm")

# Define Transistor Types
# HP = High Performance (Desktop), LSTP = Low Standby Power (Mobile)
types=("itrs-hp" "itrs-lstp")
type_labels=("HP" "LSTP")

CACTI_TOOL="../cacti"

# Double Loop: Tech Node AND Transistor Type
for ((i=0; i<${#techs[@]}; i++)); do
    curr_tech=${techs[$i]}
    curr_tech_lbl=${tech_labels[$i]}

    for ((j=0; j<${#types[@]}; j++)); do
        curr_type=${types[$j]}
        curr_type_lbl=${type_labels[$j]}
        
        # File Naming: tech_22nm_type_HP.cfg
        cfg_name="configs/tech_${curr_tech_lbl}_type_${curr_type_lbl}.cfg"
        out_name="runs/tech_${curr_tech_lbl}_type_${curr_type_lbl}.txt"
        
        # 1. Start with Baseline
        cp configs/baseline.cfg $cfg_name
        
        # 2. Set Tech Node
        sed -i "s/-technology (u) 0.022/-technology (u) $curr_tech/" $cfg_name
        
        # 3. Set Transistor Type (Replace ALL occurrences of itrs-hp)
        # We use 'g' (global) to replace it for Data Array AND Tag Array
        sed -i "s/\"itrs-hp\"/\"$curr_type\"/g" $cfg_name
        
        # 4. Run Simulation
        echo "Running: $curr_tech_lbl using $curr_type_lbl transistors..."
        (cd .. && ./cacti -infile exp2_tech_scaling/$cfg_name > exp2_tech_scaling/$out_name)
    done
done

echo "HP vs LSTP Simulation Complete!"