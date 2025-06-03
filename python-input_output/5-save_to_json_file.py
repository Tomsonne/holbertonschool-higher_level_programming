#!/usr/bin/python3
"""READ"""
import json


def save_to_json_file(my_obj, filename):
    """Write"""

    with open(filename, "w") as f:
        json_str = json.dumps(my_obj)

        return f.write(json_str)
