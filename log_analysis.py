import csv
from collections import Counter

# Function to parse the log file and return a list of log entries
def parse_log(file_path):
    with open(file_path, 'r') as file:
        log_entries = file.readlines()
    return log_entries

# Function to count requests per IP address
def count_requests_per_ip(log_entries):
    ip_counter = Counter()
    for line in log_entries:
        # Extract the IP address (assuming it's the first value in each line)
        parts = line.split()
        ip_address = parts[0]
        ip_counter[ip_address] += 1
    return ip_counter

# Function to identify the most accessed endpoint
def identify_most_accessed_endpoint(log_entries):
    endpoint_counter = Counter()
    for line in log_entries:
        # Extract the endpoint from the log line (assumed to be in quotes)
        parts = line.split('"')
        if len(parts) > 1:
            request = parts[1].split(" ")
            endpoint = request[1]  # the endpoint is the second part of the request
            endpoint_counter[endpoint] += 1
    return endpoint_counter

# Function to detect suspicious activity based on failed login attempts
def detect_suspicious_activity(log_entries, threshold=10):
    failed_login_counter = Counter()
    for line in log_entries:
        # Check for failed login attempts (HTTP status code 401 or "Invalid credentials")
        if '401' in line or 'Invalid credentials' in line:
            parts = line.split()
            ip_address = parts[0]
            failed_login_counter[ip_address] += 1

    # Filter out IP addresses that have failed attempts above the threshold
    suspicious_ips = {ip: count for ip, count in failed_login_counter.items() if count > threshold}
    return suspicious_ips

# Function to save the results to a CSV file
def save_to_csv(ip_counts, endpoint_counts, suspicious_activity, output_file='log_analysis_results.csv'):
    # Writing results to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Address', 'Request Count'])
        for ip, count in ip_counts.items():
            writer.writerow([ip, count])

        writer.writerow([])
        writer.writerow(['Endpoint', 'Access Count'])
        for endpoint, count in endpoint_counts.items():
            writer.writerow([endpoint, count])

        writer.writerow([])
        writer.writerow(['IP Address', 'Failed Login Count'])
        for ip, count in suspicious_activity.items():
            writer.writerow([ip, count])

# Main function to run the log analysis
def main():
    log_file_path = 'sample.log'  # Change the file path if necessary
    log_entries = parse_log(log_file_path)

    # Count requests per IP
    ip_counts = count_requests_per_ip(log_entries)
    
    # Identify most accessed endpoint
    endpoint_counts = identify_most_accessed_endpoint(log_entries)

    # Detect suspicious activity (failed login attempts)
    suspicious_activity = detect_suspicious_activity(log_entries, threshold=10)

    # Display results in the terminal
    print("Requests per IP Address:")
    for ip, count in ip_counts.most_common():
        print(f"{ip} : {count}")
    
    print("\nMost Accessed Endpoint:")
    most_accessed = endpoint_counts.most_common(1)
    if most_accessed:
        endpoint, count = most_accessed[0]
        print(f"{endpoint} (Accessed {count} times)")
    
    print("\nSuspicious Activity Detected:")
    for ip, count in suspicious_activity.items():
        print(f"{ip} : {count}")

    # Save the results to a CSV file
    save_to_csv(ip_counts, endpoint_counts, suspicious_activity)

if __name__ == '__main__':
    main()
