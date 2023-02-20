
# AndroZoo APK Downloader

You can download as many APK files as you want using the AndroZoo API.

## Deployment

You can run the project on any Python interpreter.


[Requirement 1] First, you must apply for an API key from the AndroZoo website. (Add the link to the "androzoo@uni.lu" email address for the API key)

[Requirement 2] You must download the list of APK files available on the AndroZoo website. (Add the link to the "APK list" section: https://androzoo.uni.lu/lists)

## Demo

After meeting the requirements, you can start by splitting the 22-million-row Excel file into smaller pieces using "excel-split". You can filter the APK files you want to download using "filter-excel", or you can do it manually on the Excel file. Once you have prepared the Excel file, you can download as many APK files as you want by specifying the file location in the "downloader" file. However, be careful to check if the APK files are malware or benign when preparing the Excel file.

