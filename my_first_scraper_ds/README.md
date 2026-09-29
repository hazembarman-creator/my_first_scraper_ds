# Welcome to My First Scraper DS
A Python web‑scraping project designed to extract trending repositories from GitHub, transform the data, and format it for output. The project also includes automated tests that validate each step of the scraping pipeline.

***

## Task
The main challenge in this project is not the scraper itself — the scraping logic works — but the **test cases**, which currently fail due to incorrect handling of response objects and extracted data.

The tasks include:

1. **Requesting GitHub Trending page**
2. **Extracting repository elements from HTML**
3. **Transforming extracted elements into dictionaries**
4. **Formatting the final output into a readable string**
5. **Passing all automated tests**

The failing tests highlight issues such as:

- `extract()` returning a Response instead of parsed elements  
- `transform()` not producing enough items  
- `format()` not returning a string  
- Incorrect handling of `requests.Response` objects  

Fixing these ensures the scraper behaves correctly and passes all test cases.

***

## Description
The solution is implemented through a clear scraping pipeline:

### **1. request_github_trending(url)**
- Sends an HTTP GET request using `requests.get()`
- Uses a User‑Agent header to avoid blocking
- Returns a `requests.Response` object

### **2. extract(page)**
- Accepts either a Response or raw HTML
- Parses HTML using **BeautifulSoup**
- Finds all elements with class `Box-row`
- Returns a list of repository HTML blocks

### **3. transform(repos)**
- Iterates through each repository element
- Extracts:
  - Developer name  
  - Repository name  
  - Number of stars  
- Stores each repo as a dictionary
- Returns a list of dictionaries

### **4. format(list_of_dicts)**
- Converts each dictionary into a formatted string
- Concatenates all strings into one output
- Returns a final string

### **Main Execution**
- Defines the GitHub Trending URL  
- Calls all functions in order  
- Prints the final formatted output  

This pipeline can be customized by changing the URL or adding more extraction logic.

***

## Installation
To run this scraper, install:

- **Python 3.6+**
- **requests**
- **beautifulsoup4**

Install dependencies:

```bash
pip install requests beautifulsoup4
No additional tools (npm, make, etc.) are required.

Usage
The scraper works by importing the necessary libraries:

python
import requests
from bs4 import BeautifulSoup
import csv
Run the script:

bash
python my_first_scraper_ds.py
Or using your project runner:

bash
./my_project argument1 argument2
Arguments may include:

URL

Output file

Mode (extract / transform / format)

You can adjust them depending on your workflow.

The Core Team
Hazem — Developer & Scraper Architect

Team Member (Testing) — Identified failing test cases and validated fixes

Team Member (Documentation)
