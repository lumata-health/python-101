from pathlib import Path
import pandas as pd

# --- CONFIG ---
FILE = Path(r"data/file.xlsx")  # or .csv
N_HEAD = 10
N_TAIL = 10

ext = FILE.suffix.lower()

if ext == ".csv":
    df = pd.read_csv(FILE)
    sample_path = FILE.with_name(FILE.stem + "_SAMPLE.csv")

elif ext == ".xlsx":
    df = pd.read_excel(FILE, engine="openpyxl")
    sample_path = FILE.with_name(FILE.stem + "_SAMPLE.xlsx")

else:
    raise SystemExit("Unsupported file type. Use .csv or .xlsx")

# Columns
print("=== Columns ===")
print(df.columns.tolist())

# Head / Tail
head = df.head(N_HEAD)
tail = df.tail(N_TAIL)

print(f"\n=== First {len(head)} rows ===")
print(head)

print(f"\n=== Last {len(tail)} rows ===")
print(tail)

# Save sample file: header + head + tail (no de-dup)
sample_df = pd.concat([head, tail], ignore_index=True)

if ext == ".csv":
    sample_df.to_csv(sample_path, index=False)
else:  # .xlsx
    sample_df.to_excel(sample_path, index=False)

print(f"\nSample file written to: {sample_path}")
