#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """Print metrics based on total size and status codes."""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """Parse line and update metrics."""
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]
        total_size += size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

    except (ValueError, IndexError):
        pass  # Ignore lines with incorrect format

    return total_size, status_codes

if __name__ == "__main__":
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_codes = parse_line(line.strip(), total_size, status_codes)

            if i % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
