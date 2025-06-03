#!/usr/bin/python3
"""Read"""
import json


def load_from_json_file(filename):
    """Load"""

    with open(filename, "r") as f:
        return json.load(f)
