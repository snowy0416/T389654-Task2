# T389654-Task2

This repository contains my submission for **Task 2** of Addressing the new Lusophone technological wishlist proposals.

## Task Description
The task involves creating a Python script to check the status codes of URLs from a CSV file. The script reads the URLs, sends HTTP requests, and prints the status codes in the following format:
(STATUS CODE) URL

## Key Features
- 🚀 Multi-threaded URL processing (ThreadPoolExecutor)
- 🛡️ Robust URL validation (checks schemes, domains, and formats)
- 📊 Color-coded console output (green=success, red=errors)
- 📂 Automatic CSV logging (valid and invalid URLs)

## Files
- `task2.py`: The Python script to check URL status codes
- `Task 2 - Intern.csv`: The input CSV file containing 166 URLs 
- `Task 2 - Results.csv`: The output CSV file containing the results
- `Invalid_URLs.csv`: Logs all malformed URLs with rejection reasons
- `test_urls.csv`: Sample test cases (try: `python task2.py test_urls.csv`)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/snowy0416/T389654-Task2.git
   
2. Navigate to the repository folder:
 cd T389654-Task2
 
3. Install the required libraries:
 pip install requests

4. Run the script:
 python task2.py# Uses default CSV

 For custom files:
 python task2.py your_urls.csv

## Dependencies
Python 3.x

requests library (install using pip install requests)



