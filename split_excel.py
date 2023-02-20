import pandas as pd

filename = 'latest.csv'
chunksize = 500000
output_prefix = 'output_'
chunk_number = 1

for chunk in pd.read_csv(filename, chunksize=chunksize):
    output_filename = output_prefix + str(chunk_number) + '.csv'
    chunk.to_csv(output_filename, index=False)
    print(f"{chunk_number}. chunk created.")
    chunk_number += 1

