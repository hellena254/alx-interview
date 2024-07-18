#!/usr/bin/python3

"""
Log Parsing
"""

import sys
import signal

total_sizes = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_statistics():
    """Print the stats collected"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys());
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    """Handle keyboard interrupt signal"""
    print_statistics()
    sys.exit(0)
