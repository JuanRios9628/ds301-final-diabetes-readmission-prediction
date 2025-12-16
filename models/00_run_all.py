import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "diabetic_data.csv"

def main():
    df = pd.read_csv(DATA_PATH)
    print("Shape:", df.shape)

    if "readmitted" in df.columns:
        print("\nTarget distribution (readmitted):")
        print(df["readmitted"].value_counts(dropna=False))
    else:
        print("ERROR: 'readmitted' column not found.")

if __name__ == "__main__":
    main()
