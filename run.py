import pandas as pd
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Traffic Analysis')
    parser.add_argument('--data', required=True, help='Path to CSV file')
    parser.add_argument('--target', required=True, help='Target column name')
    
    args = parser.parse_args()
    
    print(f"Loading data from: {args.data}")
    print(f"Target column: {args.target}")
    
    try:
        # Load data
        df = pd.read_csv(args.data)
        print(f"Data loaded successfully! Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        # Check if target column exists
        if args.target in df.columns:
            print(f"✅ Target column '{args.target}' found!")
            print(f"Target column stats:")
            print(df[args.target].describe())
        else:
            print(f"❌ Target column '{args.target}' not found!")
            print(f"Available columns: {list(df.columns)}")
            print("\nTry one of these as your target:")
            for col in df.columns:
                print(f"  --target {col}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()