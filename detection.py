import os
import re
import csv

CSV_FILE = "api_list.csv"
LOG_FILE = "log.txt"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["api"])

def read_apis_from_csv():
    with open(CSV_FILE, "r") as f:
        return {row[0] for row in csv.reader(f) if row}

def write_apis_to_csv(new_apis):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for api in new_apis:
            writer.writerow([api])

def scan_apis():
    apis = set()
    pattern = re.compile(r"@*\.\(['\"](/[^'\"]+)['\"]")
    for file in os.listdir('.'):
        if file.endswith('.py') and file != __file__:
            with open(file, 'r') as f:
                apis.update(pattern.findall(f.read()))
    return apis

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

if __name__ == '__main__':
    existing_apis = read_apis_from_csv()
    current_apis = scan_apis()
    new_apis = current_apis - existing_apis

    if new_apis:
        for api in new_apis:
            log_message(f"New API detected: {api}")
        write_apis_to_csv(new_apis)
    else:
        log_message("No new APIs detected.")
