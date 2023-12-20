#!/bin/bash

# Execute the data pipeline
./project/pipeline.sh

# Check if the output files exist
if [ -f "data/Twitch_game_data.csv" ]; then
    echo "Data pipeline completed successfully!"
else
    echo "Error: Data pipeline failed to create output files."
    exit 1
fi

# Seems like the pipeline runs successfully and can download the Kaggle twitch.csv database through the workflow.
# But the tests.sh fails to find the downloaded files, thus returning the below error.
# Works fine in local but this seems to be an issue when running through workflow.  

# Downloaded files: ['Twitch_global_data.csv', 'Twitch_game_data.csv']
# Data pipeline completed successfully!
# Error: Data pipeline failed to create output files.
# Error: Process completed with exit code 1.
