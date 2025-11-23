#!/bin/bash

# Banks to test (Powers of 2)
banks=(1 2 4 8 16 32 64)

# Create configs for each bank count
mkdir -p configs_banking
mkdir -p runs_banking

# Baseline is your L3 Huge from the previous step
BASE="configs/L3_huge.cfg"

for b in "${banks[@]}"; do
    
    cfg="configs_banking/L3_8MB_banks_${b}.cfg"
    out="runs_banking/L3_8MB_banks_${b}.txt"
    
    # 1. Copy the 8MB L3 config
    cp $BASE $cfg
    
    # 2. Modify Bank Count
    # We change "-UCA bank count 1" to whatever 'b' is
    sed -i "s/-UCA bank count 1/-UCA bank count $b/" $cfg
    
    # 3. Run CACTI
    echo "Simulating 8MB L3 with $b Banks..."
    (cd .. && ./cacti -infile exp3_hierarchy/$cfg > exp3_hierarchy/$out)
    
done

echo "Banking Optimization Complete!"