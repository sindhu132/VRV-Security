import re
import csv
from collections import defaultdict

def preprocess_log(input_path, output_path):
    """
    Preprocess the log file to ensure it matches the expected format.
    """
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            # Example: Preprocess by ensuring all fields are present
            parts = line.strip().split()
            if len(parts) < 7:  # Example: Log lines with fewer than 7 parts are skipped
                continue
            try:
                formatted_line = f"{parts[0]} - - [{parts[3][1:]}] \"{parts[5]} {parts[6]} {parts[7]}\" {parts[8]} {parts[9]}"
                outfile.write(formatted_line + '\n')
            except IndexError:
                continue

def parse_log(file_path):
    """
    Parse the log file and extract information.
    """
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<method>[A-Z]+) (?P<endpoint>/\S*) HTTP/1.1" (?P<status>\d+) (?P<size>\d+)(?: "(?P<message>.*?)")?'
    )
    
    ip_counts = defaultdict(int)
    endpoint_counts = defaultdict(int)
    failed_login_attempts = defaultdict(int)

    with open(file_path, 'r') as log_file:
        for line in log_file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                ip = data['ip']
                endpoint = data['endpoint']
                status = data['status']

                ip_counts[ip] += 1
                endpoint_counts[endpoint] += 1

                if status == '401':  # Unauthorized access
                    failed_login_attempts[ip] += 1

    return ip_counts, endpoint_counts, failed_login_attempts

def find_most_frequent(data_dict):
    """
    Find the most frequent item in a dictionary.
    """
    if not data_dict:
        return None, 0
    return max(data_dict.items(), key=lambda x: x[1])

def save_to_csv(ip_counts, endpoint_counts, failed_login_attempts, output_file):
    """
    Save the results to a CSV file.
    """
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Item", "Count"])
        writer.writerow(["Most Frequent IP", *find_most_frequent(ip_counts)])
        writer.writerow(["Most Frequent Endpoint", *find_most_frequent(endpoint_counts)])
        writer.writerow([])
        writer.writerow(["Detailed Counts"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_counts.items():
            writer.writerow([ip, count])
        writer.writerow([])
        writer.writerow(["Endpoint", "Request Count"])
        for endpoint, count in endpoint_counts.items():
            writer.writerow([endpoint, count])
        writer.writerow([])
        writer.writerow(["IP Address", "Failed Login Attempts"])
        for ip, count in failed_login_attempts.items():
            writer.writerow([ip, count])

def main():
    # Replace these file paths with your actual paths
    raw_log_file = "C:/Users/HP/Documents/raw_log_file.txt"
    processed_log_file = "C:/Users/HP/Documents/processed_log_file.txt"
    output_csv = "C:/Users/HP/Documents/log_analysis_results.csv"


    print("Preprocessing log file...")
    preprocess_log(raw_log_file, processed_log_file)
    print("Log preprocessing complete.")

    print("Analyzing log file...")
    ip_counts, endpoint_counts, failed_login_attempts = parse_log(processed_log_file)

    most_frequent_endpoint, endpoint_count = find_most_frequent(endpoint_counts)
    print(f"Most Frequently Accessed Endpoint: {most_frequent_endpoint} ({endpoint_count} times)")

    if any(failed_login_attempts.values()):
        print("Suspicious activity detected:")
        for ip, count in failed_login_attempts.items():
            print(f"IP: {ip} - Failed Login Attempts: {count}")
    else:
        print("No suspicious activity detected.")

    print("Saving results to CSV...")
    save_to_csv(ip_counts, endpoint_counts, failed_login_attempts, output_csv)
    print(f"Results saved to {output_csv}")

if __name__ == "__main__":
    main()
