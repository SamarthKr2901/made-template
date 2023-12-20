#!/bin/bash

# Execute the data pipeline
./project/pipeline.sh

# Check if the output files exist
if [ -f "data/data.sqlite" ]; then
    echo "Data pipeline completed successfully!"
else
    echo "Error: Data pipeline failed to create output files."
    exit 1
fi

# Seems like the pipeline is not able to download the Kaggle twitch.csv database through the workflow, although it is working perfectly fine in my Local.
# The csv fails to download which results in data.sqlite not being created, thus failing the pipeline and the test, returning the below error.  

# FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/made-template/made-template/../data/Twitch_game_data.csv'
# Error: Data pipeline failed to create output files.
# Error: Process completed with exit code 1.
