import requests
import pandas as pd
import concurrent.futures
import os

if not os.path.exists("malware"):
    os.makedirs("malware")

endpoint = "https://androzoo.uni.lu/api/download"

api_key = "your-api-key"

file_name = "filtered_data.xlsx"

sha256_column = "sha256"

# you can change below, how many apk u need
start_row = 0
end_row = 25000

df = pd.read_excel(file_name, usecols=[sha256_column], nrows=end_row)

def download_file(sha256, i):
    file_name = os.path.join("malware", sha256 + ".apk")
    url = endpoint + f"?apikey={api_key}&sha256={sha256}"
    print(f"Downloading file {i}/{end_row-start_row} with SHA256 {sha256}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    else:
        print(f"File download failed for SHA256 {sha256}.")

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    futures = []
    for i, sha256 in enumerate(df[sha256_column].iloc[start_row:end_row], start=1):
        futures.append(executor.submit(download_file, sha256, i))
    for future in concurrent.futures.as_completed(futures):
        if future.exception() is not None:
            print(f"File download failed with exception: {future.exception()}")

