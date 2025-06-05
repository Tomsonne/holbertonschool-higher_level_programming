#!/usr/bin/python3
"""
BIIIP
bip
"""
import json
import csv


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r') as f:
            read = csv.DictReader(f)
            read_data = list(read)
            with open("data.json", 'w') as f2:
                json.dump(read_data, f2)
        return True
    except (FileNotFoundError, csv.Error):
        return False