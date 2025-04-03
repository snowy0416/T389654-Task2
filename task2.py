import requests
import csv
import sys  # Added for command-line arguments
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

# Initialize colorama for colored console output
init(autoreset=True)

def is_valid_url(url):
    """Strict URL validation with detailed feedback"""
    url = str(url).strip()
    if not url or url.lower() in ('urls', 'url'):
        return False, "Header/empty row"
    
    try:
        parsed = urlparse(url)
        if not parsed.scheme or parsed.scheme not in ('http', 'https'):
            return False, "Missing http:// or https://"
        if not parsed.netloc or '.' not in parsed.netloc:
            return False, "Invalid domain"
        return True, "Valid"
    except Exception as e:
        return False, f"Malformed URL: {str(e)}"

def check_url(url):
    """Check URL status with detailed error handling"""
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        return response.status_code
    except requests.exceptions.SSLError:
        return "SSL Error"
    except requests.exceptions.ConnectionError:
        return "Connection Failed"
    except requests.exceptions.Timeout:
        return "Timeout"
    except requests.exceptions.RequestException as e:
        return f"Error: {type(e).__name__}"

def get_status_color(status):
    """Return color based on status code"""
    if isinstance(status, int):
        if 200 <= status < 300:
            return Fore.GREEN
        elif 400 <= status < 500:
            return Fore.YELLOW
        elif status >= 500:
            return Fore.RED
    return Fore.MAGENTA  # For custom error messages

def main():
    # Get input file from command line or use default
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'Task 2 - Intern.csv'
    
    # Read URLs
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        urls = [row[0].strip() for row in reader if row and row[0].strip()]
    
    total_urls = len(urls)
    print(f"\n{Fore.CYAN}Processing {total_urls} URLs from {input_file}{Style.RESET_ALL}")

    # Prepare output files
    with open('Task 2 - Results.csv', 'w', newline='', encoding="utf-8") as res_f, \
         open('Invalid_URLs.csv', 'w', newline='', encoding="utf-8") as inv_f:

        res_writer = csv.writer(res_f)
        inv_writer = csv.writer(inv_f)
        
        # Write headers
        res_writer.writerow(['Result'])
        inv_writer.writerow(['URL', 'Reason'])

        valid_urls = []
        invalid_count = 0

        # Validation phase
        for url in urls:
            is_valid, reason = is_valid_url(url)
            if is_valid:
                valid_urls.append(url)
            else:
                inv_writer.writerow([url, reason])
                invalid_count += 1
                print(f"{Fore.RED}(INVALID) {url} - {reason}{Style.RESET_ALL}")

        # Processing phase
        success_count = 0
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(check_url, url): url for url in valid_urls}
            for future in as_completed(futures):
                url = futures[future]
                status = future.result()
                formatted_result = f"({status}) {url}"
                
                # Write to CSV
                res_writer.writerow([formatted_result])
                
                # Colorized console output
                status_color = get_status_color(status)
                print(f"{status_color}{formatted_result}{Style.RESET_ALL}")
                
                success_count += 1

    # Final report
    print(f"\n{Fore.CYAN}=== Processing Complete ===")
    print(f"Total URLs: {total_urls}")
    print(f"Successfully checked: {success_count}")
    print(f"Invalid URLs: {invalid_count}")
    print(f"Results saved to:")
    print(f"- Task 2 - Results.csv")
    print(f"- Invalid_URLs.csv{Style.RESET_ALL}")

if __name__ == "__main__":
    main()