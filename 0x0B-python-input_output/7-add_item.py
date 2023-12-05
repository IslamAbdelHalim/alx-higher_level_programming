#!/usr/bin/python3
"""add all arguments to python list"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"
# load file and check the file is exist
try:
    file = load_from_json_file(file)
except (ValueError, FileNotFoundError):
    file = []

for arg in sys.argv[1:]:
    file.append(arg)

# save to file
save_to_json_file(file, "add_item.json")
