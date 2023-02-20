import pandas as pd
import glob

csv_files = glob.glob("output_*.csv")

filtered_df = pd.DataFrame()

for file in csv_files:
    print(f"Processing file: {file}")
    
    df = pd.read_csv(file)
    
    df = df[(df["vt_detection"] >= 10) & (df["apk_size"] < 2000000)]
    df = df.sort_values(by=["vt_detection"], ascending=False)
    
    filtered_df = pd.concat([filtered_df, df], ignore_index=True)
    
filtered_df.to_excel("filtered_data.xlsx", index=False)
