
# VRV Security’s Python Intern Assignment
 Log Analysis Project

This Python project analyzes web server logs and extracts key insights such as IP request counts, the most frequently accessed endpoints, and suspicious activity (e.g., brute-force login attempts).

## Features
- **IP Request Count**: Counts the number of requests made by each IP address.
- **Most Frequently Accessed Endpoint**: Identifies the endpoint that was accessed the most.
- **Suspicious Activity Detection**: Detects potential brute-force login attempts by flagging IP addresses with excessive failed login attempts.

## Prerequisites
- Python 3.x
- Required Python packages:
    - `pandas` (for data manipulation)
    - `csv` (for CSV handling)
    - `re` (for regular expressions)


Place your log file (`sample.log`) in the project folder.

## Usage

To run the script, simply execute the following command:

python log_analysis.py

markdown
Copy code

The script will:
- Analyze the log file (`sample.log`).
- Output the results in the terminal.
- Save the results in a CSV file: `log_analysis_results.csv`.

## Output

- **IP Request Count**: A table showing the request count for each IP.
- **Most Accessed Endpoint**: The endpoint accessed the most number of times.
- **Suspicious Activity**: A list of IP addresses with failed login attempts exceeding a configurable threshold.

