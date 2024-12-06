import csv
import re
from collections import defaultdict

# Function to parse the log file and extract necessary details
def parse_log(file_path):
    log_pattern = re.compile(
        r'(?P<ip_address>\d+\.\d+\.\d+\.\d+) - - '
        r'\[(?P<timestamp>[^\]]+)\] '
        r'"(?P<method>GET|POST|PUT|DELETE|PATCH|OPTIONS) (?P<endpoint>[^\s]+) (?P<http_version>HTTP/\d+\.\d+)" '
        r'(?P<status_code>\d{3}) (?P<size>\d+)(?: "(?P<additional_info>.*)")?'
    )

    ip_counts = defaultdict(int)
    endpoint_counts = defaultdict(int)
    failed_login_attempts = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                ip = data['ip_address']
                endpoint = data['endpoint']
                status_code = data['status_code']
                additional_info = data.get('additional_info', '')

                # Count requests per IP
                ip_counts[ip] += 1

                # Count requests per endpoint
                endpoint_counts[endpoint] += 1

                # Identify failed login attempts (status code 401 and relevant additional info)
                if status_code == '401' and 'Invalid credentials' in additional_info:
                    failed_login_attempts[ip] += 1

    return ip_counts, endpoint_counts, failed_login_attempts

# Function to save results to a CSV file
def save_to_csv(ip_counts, endpoint_counts, failed_login_attempts, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Section 1: Requests per IP
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_counts.items():
            writer.writerow([ip, count])

        # Section 2: Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        for endpoint, count in sorted(endpoint_counts.items(), key=lambda x: -x[1]):
            writer.writerow([endpoint, count])

        # Section 3: Suspicious Activity
        writer.writerow([])
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in failed_login_attempts.items():
            writer.writerow([ip, count])

# Main function
def main():
    log_file_path = "C:/Users/HP/Documents/raw_log_file.txt"  # Path to your raw log file
    output_csv_file = "C:/Users/HP/Documents/log_analysis_results.csv"  # Output CSV file path

    print("Analyzing log file...")
    ip_counts, endpoint_counts, failed_login_attempts = parse_log(log_file_path)
    
    print("Saving results to CSV...")
    save_to_csv(ip_counts, endpoint_counts, failed_login_attempts, output_csv_file)
    
    print(f"Analysis complete. Results saved to {output_csv_file}")

if __name__ == "__main__":
    main()
