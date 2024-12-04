
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

## Setup

1. Clone the repository:
git clone https://github.com/yourusername/log-analysis.git

markdown
Copy code

2. Install the required Python packages:
pip install pandas

bash
Copy code

3. Place your log file (`sample.log`) in the project folder.

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

## Example Log File

Here is a sample entry from the log file:

192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512 203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"

python
Copy code

## License

This project is open source and available under the [MIT License](LICENSE)
Explanation:
Project Title and Description: A brief overview of what the project is.
Features: Short description of the key functionalities.
Prerequisites: The necessary tools and packages for running the project.
Setup: Instructions for setting up the project locally.
Usage: Instructions on how to run the project.
Output: What the script generates (both in terminal and in CSV).
Sample Log File: Provides an example of what the log file looks like.
License: Licensing information (you can modify or remove this depending on your prefe
