import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlparse
from urllib.request import urlopen

# Function to calculate the page weight of a website
def calculate_page_weight(url):
    try:
        #http request
        response = requests.get(url)
        response.raise_for_status()

        #Parsing html data of page
        soup = BeautifulSoup(response.text, 'html.parser')

        #size of the HTML data
        html_size = len(response.text)

        total_page_weight = 0
        total_page_weight += html_size

        #finding all resources (images, scripts, stylesheets, etc.) in the HTML data
        resources = soup.find_all(['img', 'script', 'link', 'style'])

        #loop through each resource and calculate its size
        for resource in resources:
            resource_url = resource.get('src') or resource.get('href')
            if resource_url:
                resource_url = urllib.parse.urljoin(url, resource_url)
                resource_response = urlopen(resource_url)
                resource_size = len(resource_response.read())
                total_page_weight += resource_size

        return total_page_weight

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch the webpage:", e)
        return None

if __name__ == "__main__":
    website_url = "https://www.google.com"  #input webpage url
    page_weight = calculate_page_weight(website_url)

    if page_weight is not None:
        print(f"Page weight of {website_url}: {page_weight} bytes")
