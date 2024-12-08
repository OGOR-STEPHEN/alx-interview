#!/usr/bin/python3
"""
Module to read stdin line by line and compute metrics based on input format.
"""

import sys

def print_stats(total_size, status_counts):
    """Print the statistics for total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    """Main function to read lines from stdin and process metrics."""
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            try:
                # Extract file size and status code
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                # Update total size
                total_size += file_size

                # Update status code count if valid
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (IndexError, ValueError):
                # Skip lines that don't match the expected format
                continue

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()

