#!/usr/bin/python3
'''
Script for parsing HTTP request logs and computing metrics.

This script reads HTTP request logs from stdin, parses each line to extract
relevant information (status code and file size), and computes the following metrics:
- Total file size accumulated.
- Number of occurrences for each HTTP status code encountered.

The script prints these metrics after every 10 lines of input or on keyboard interruption (CTRL + C).
'''

import re
import sys
import signal

def parse_log_entry(input_line):
    '''
    Parses a line of HTTP request log to extract status code and file size.

    Args:
        input_line (str): A line from the HTTP request log.

    Returns:
        dict: Dictionary containing 'status_code' and 'file_size' extracted from the input line.
    '''
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    format_str = '{}\\-{}{}{}{}\\s*'.format(*pattern)
    match = re.fullmatch(format_str, input_line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        return {'status_code': status_code, 'file_size': file_size}
    return {'status_code': None, 'file_size': 0}

def print_metrics(total_size, status_codes_counts):
    '''
    Prints accumulated metrics of HTTP request logs.

    Args:
        total_size (int): Total accumulated file size.
        status_codes_counts (dict): Dictionary containing counts of each status code.
    '''
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_codes_counts.keys()):
        count = status_codes_counts.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)

def update_metrics(line, total_size, status_codes_counts):
    '''
    Updates metrics from a given line of HTTP request log.

    Args:
        line (str): Line of input from which to retrieve metrics.
        total_size (int): Current total file size.
        status_codes_counts (dict): Dictionary containing counts of each status code.

    Returns:
        int: Updated total file size.
    '''
    log_info = parse_log_entry(line)
    status_code = log_info.get('status_code', '0')
    if status_code in status_codes_counts.keys():
        status_codes_counts[status_code] += 1
    return total_size + log_info['file_size']

def start_parser():
    '''
    Starts the log parser.
    '''
    line_num = 0
    total_size = 0
    status_codes_counts = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        while True:
            line = input()
            total_size = update_metrics(
                line,
                total_size,
                status_codes_counts,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_metrics(total_size, status_codes_counts)
    except (KeyboardInterrupt, EOFError):
        print_metrics(total_size, status_codes_counts)

if __name__ == '__main__':
    start_parser()
