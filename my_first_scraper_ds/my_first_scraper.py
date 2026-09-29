import requests
from bs4 import BeautifulSoup
import csv

def request_github_trending(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    return response

def extract(page):
    if isinstance(page, requests.Response):
        # Handle the case when the page is a Response object
        html_content = page.content
    else:
        # Assume the page is already HTML content
        html_content = page

    soup = BeautifulSoup(html_content, 'html.parser')
    html_repos = soup.find_all('article', {'class': 'Box-row'})
    return html_repos

def transform(html_repos):
    repositories_data = []
    for repo in html_repos:
        developer = repo.find('span', {'class': 'd-inline-block'}).text.strip()
        repo_name = repo.find('h1', {'class': 'h3'}).text.strip()
        stars = repo.find('a', {'class': 'Link--muted'}).text.strip()
        repository = {
            'developer': developer,
            'repository_name': repo_name,
            'nbr_stars': stars
        }
        repositories_data.append(repository)
    return repositories_data

def format(array_of_dict):
    output_str = ""
    for repo in array_of_dict:
        output_str += f"Developer: {repo['developer']}\n"
        output_str += f"Repository: {repo['repository_name']}\n"
        output_str += f"Stars: {repo['nbr_stars']}\n\n"
    return output_str.strip()
