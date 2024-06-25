#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys

total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 1, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines = 0


def print_stats():
    print(f"File size: {total_file_size}")
    for k, v in status_codes.items():
        if v != 0:
            print(f"{k}: {v}")


try:
    for line in sys.stdin:
        tokens = line.split(" ")
        try:
            file_size = int(tokens[-1])
            total_file_size += file_size

            status_code = int(tokens[-2])
            if status_code in list(status_codes):
                status_codes[status_code] += 1
        except ValueError:
            pass
        lines += 1
        if lines % 10 == 0:
            print_stats()
    if lines == 0 or lines != 10:
        print_stats()
except KeyboardInterrupt:
    print_stats()
