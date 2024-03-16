import requests
from bs4 import BeautifulSoup
import random

def scrape_random_wikipedia_page():
    # Fetch a random Wikipedia page
    random_page_url = "https://en.wikipedia.org/wiki/FIFA_World_Cup"
    response = requests.get(random_page_url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.find("h1", {"id": "firstHeading"}).text
        
        # Try to find content, handling None if not found
        content_div = soup.find("div", {"id": "content"})
        if content_div:
            content_paragraphs = content_div.find_all("p")
            content = "\n".join([para.text for para in content_paragraphs])
            return title, content
        else:
            print("Content not found on the page.")
            return title, None
    else:
        print("Failed to fetch random Wikipedia page.")
        return None, None

if __name__ == "__main__":
    title, content = scrape_random_wikipedia_page()
    if title:
        print("Title:", title)
        if content:
            print("Content:")
            print(content)
        else:
            print("No content found.")
