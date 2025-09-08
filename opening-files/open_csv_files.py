from collections import deque
from pathlib import Path
import csv

path = Path(r'example.csv')  # REPLACE FILE PATH HERE
N_HEAD = 10
N_TAIL = 10

with path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)

    header = None
    first_rows = []
    last_rows = deque(maxlen=N_TAIL)
    count = 0

    for row in reader:
        # Remove empty rows
        if (not row) or all(str(c).strip() == "" for c in row):
            continue

        # First non-empty line becomes header
        if header is None:
            header = row
            continue

        # Accumulate first N and rolling last N
        count += 1
        if count <= N_HEAD:
            first_rows.append(row)
        last_rows.append(row)

# Print summary to console
if header is None:
    print("Empty file or missing header.")
else:
    print("Columns")
    print(header)

    print(f"\nFirst {min(N_HEAD, count)} rows")
    for r in first_rows:
        print(r)

    print(f"\nLast {min(N_TAIL, count)} rows")
    for r in last_rows:
        print(r)

    print(f"\nTotal data rows (excluding header): {count}")

    # Save small sample file: header + head(10) + tail(10)
    sample_path = path.with_name(path.stem + "_SAMPLE.csv")
    with sample_path.open("w", encoding="utf-8", newline="") as out:
        w = csv.writer(out)
        w.writerow(header)

        combined = list(first_rows) + list(last_rows)

        for r in combined:
            w.writerow(r)

    print(f"\nSample file written to: {sample_path}")
