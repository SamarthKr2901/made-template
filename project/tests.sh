#!/bin/bash

# Execute the data pipeline
python3 pipeline.py

# Check if the output files exist
if [ -f "../data/data.sqlite" ]; then
    echo "Data pipeline completed successfully!"
else
    echo "Error: Data pipeline failed to create output files."
    exit 1
fi

# Add system-test level test case here