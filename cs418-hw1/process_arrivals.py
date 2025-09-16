import json
import os
import pandas as pd

# 3% credit
def extract_arrival_data_from_files(directory):
    """
    Extracts scheduled and actual arrival data from all JSON files in a directory.

    Args:
        directory (str): The path to the directory containing the JSON files.

    Returns:
        tuple: A tuple containing two lists:
               - all_actual_arrivals (list): A list of all actual arrival times.
               - all_scheduled_arrivals (list): A list of all scheduled departure times.
    """
    all_actual_arrivals = []
    all_scheduled_arrivals = []
    
    # Assuming the files are named like '2024080X.json'
    for i in range(1, 8): # Loop to get 7 files
        # This creates filenames like 20240801.json, 20240802.json ... 20240807.json
        # You might need to adjust the base name and range depending on your exact filenames.
        # For the provided context, we have 20240803.json to 20240807.json
        # Let's adjust to use the files we have.
        # A more robust way is to list files in the directory.
    
    json_files = [f for f in os.listdir(directory) if f.endswith('.json') and f.startswith('202408')]

    for filename in sorted(json_files):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)
            
            # Extract actual arrivals
            for stop_id in data.get('arrivals', {}):
                for arrival in data['arrivals'][stop_id]:
                    if 'arrival' in arrival:
                        all_actual_arrivals.append(arrival['arrival'])
            
            # Extract scheduled arrivals
            for stop_id in data.get('scheduled', {}):
                all_scheduled_arrivals.extend(data['scheduled'][stop_id].get('allDepartures', []))

    return all_actual_arrivals, all_scheduled_arrivals
