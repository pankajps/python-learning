#!/usr/bin/python3
import os
import sys
import json
import csv
'''
Problem Statement: Automating the process of reading and writing to files for data extraction and storage.

Detailed Scenario: A project requires automating the task of reading large data files (e.g., CSV or JSON), extracting useful information, and writing the extracted data into new files for further processing.

Usecase Approach: Use Python’s file handling functions to read the data, process it, and write the output to new files.

Tools and Modules: os, sys, json, csv
'''
file_name=input("Please provide file name for processing: ")
_, ext = os.path.splitext("file_name")
csv_file=False
json_file=False
if ext == "'.csv'":
    csv_file=True
elif ext == "'.json'":
    json_file=True

print(json_file)
print(csv_file)
