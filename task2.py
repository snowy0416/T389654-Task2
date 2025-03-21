import requests
import csv
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to check if a URL is valid
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])  # Check if URL has a scheme and network location
    except:
        return False

# Function to check the status code of a URL
def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)  # Set a timeout of 5 seconds
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Read URLs from the CSV file and write results to a new CSV file
with open('Task 2 - Intern.csv', 'r') as input_file, open('Task 2 - Results.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    writer.writerow(['Result'])  # Write header row

    next(reader)  # Skip the header row (if there is one)
    urls = [row[0] for row in reader]  # Extract URLs from the CSV file

    # Use ThreadPoolExecutor to check URLs concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        future_to_url = {executor.submit(check_url_status, url): url for url in urls if is_valid_url(url)}
        
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                status_code = future.result()
                result = f"({status_code}) {url}"  # Format the result as (STATUS CODE) URL
                writer.writerow([result])  # Write the formatted result to the output file
                print(result)  # Print the result to the console
            except Exception as e:
                result = f"(Error) {url}"  # Handle unexpected errors
                writer.writerow([result])  # Write the formatted result to the output file
                print(result)  # Print the result to the console