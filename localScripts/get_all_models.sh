#!/bin/bash

# Loop through all Python scripts ending with _saveLocal_script.py
for script in *_saveLocal_script.py
do
    # Check if file exists to avoid errors
    if [[ -f "$script" ]]; then
        echo "Running $script..."
        python3 "$script"
    else
        echo "No scripts found matching *_saveLocal_script.py"
    fi
done
    