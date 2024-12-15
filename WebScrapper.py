import requests
from bs4 import BeautifulSoup
import time
import json
import re

# Retry mechanism and data scraping function
def fetch_data_with_retries(url, retries=3, delay=2):
    """
    Fetch data from a URL with retries in case of failure.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))  # Exponential backoff
            else:
                return None

# Function to extract data using BeautifulSoup and regular expressions
def extract_data_from_html(html_content):
    """
    Extract the relevant data (links containing 'python') from the HTML content.
    """
    if not html_content:
        raise ValueError("HTML content is invalid or empty!!!")

    soup = BeautifulSoup(html_content, 'html.parser')
    titles = []

    # Regular expression to find all the links with the specific text ('python')
    for link in soup.find_all('a', href=True):
        title = link.get_text()
        if re.search(r'python', title, re.IGNORECASE):  # Looking for links containing 'python'
            titles.append(title)

    return titles

# Function to save data to a JSON file
def save_data_to_json(data, filename="scraped_data.json"):
    """
    Save the extracted data to a JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Data has been saved to {filename}")
    except Exception as e:
        print(f"Error saving data to the file: {e}")

# URL to scrape
url = "https://docs.python.org/3/"

# Fetch, extract, and save the data
html_content = fetch_data_with_retries(url)
if html_content:
    extracted_data = extract_data_from_html(html_content)
    save_data_to_json(extracted_data)
else:
    print("Failed to fetch HTML content after retries.")
