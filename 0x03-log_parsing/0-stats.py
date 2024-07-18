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

# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, dash, date_bracket, method, url, protocol, status, size = parts
        if method != '"GET' or url != '/projects/260' or protocol != 'HTTP/1.1"':
            continue

        # Update total size
        try:
            total_size += int(size)
        except ValueError:
            continue

        # Update status count
        if status in status_counts:
            status_counts[status] += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

print_statistics()
