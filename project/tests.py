# Import necessary libraries
import subprocess
import os

# Run the pipeline
subprocess.run(['python', 'Pipeline.py'])

# Check if the data.sqlite file exists
db_path = '../data/data.sqlite'
if os.path.exists(db_path):
    print("Pipeline executed successfully. 'data.sqlite' file created.")
else:
    print("Pipeline failed. 'data.sqlite' file not found.")