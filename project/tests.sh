#!/bin/bash

# Navigate to the project directory
cd project

# Execute the data pipeline
./pipeline.sh

# Check if the output files exist
if [ -f "data/data.sqlite" ]; then
    echo "Data pipeline completed successfully!"
else
    echo "Error: Data pipeline failed to create output files."
    exit 1
fi

# Navigate back to the root directory
cd ..
