# import requests
# from bs4 import BeautifulSoup
# import random
# import time

# # Function to scrape quote authors
# def scrape_quote_authors(url):
#     # Send a GET request to the URL
#     response = requests.get(url)

#     # Check if request was successful
#     if response.status_code == 200:
#         # Parse HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Find all quote authors
#         authors = soup.find_all(class_='author')

#         # Extract author names
#         author_names = [author.get_text() for author in authors]
        
#         # Remove duplicate authors
#         author_names = list(set(author_names))

#         return author_names
#     else:
#         print("Failed to retrieve page.")
#         return []

# # Main function to scrape distinct quote authors
# def main():
#     # URL of the Quotes to Scrape website
#     url = 'http://quotes.toscrape.com/'

#     # Scrape quote authors
#     quote_authors = scrape_quote_authors(url)

#     # Display distinct quote authors
#     print("Distinct Quote Authors:")
#     for author in quote_authors:
#         print(author)

# if __name__ == "__main__":
#     main()


import requests
from bs4 import BeautifulSoup
import random
import time

# Function to scrape quote authors along with additional information
def scrape_quote_authors_info(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quote authors
        authors = soup.find_all(class_='author')

        # Extract author names
        author_names = [author.get_text() for author in authors]
        
        # Remove duplicate authors
        author_names = list(set(author_names))

        # Extract additional information for each author
        author_info = []
        for author_name in author_names:
            author_url = url + f"author/{author_name.replace(' ', '-')}"
            author_response = requests.get(author_url)
            if author_response.status_code == 200:
                author_soup = BeautifulSoup(author_response.text, 'html.parser')
                nationality_tag = author_soup.find('span', class_='author-born-country')
                nationality = nationality_tag.text.strip() if nationality_tag else 'N/A'
                description_tag = author_soup.find('div', class_='author-description')
                description = description_tag.text.strip() if description_tag else 'N/A'
                date_of_birth_tag = author_soup.find('span', class_='author-born-date')
                date_of_birth = date_of_birth_tag.text.strip() if date_of_birth_tag else 'N/A'
                
                author_info.append({
                    'Name': author_name,
                    'Nationality': nationality,
                    'Description': description,
                    'Date of Birth': date_of_birth
                })
            else:
                print(f"Failed to retrieve info for {author_name}")
            
            # Adding a small delay to avoid overwhelming the server
            time.sleep(1)

        return author_info
    else:
        print("Failed to retrieve page.")
        return []

# Main function to scrape distinct quote authors with additional information
def main():
    # URL of the Quotes to Scrape website
    url = 'http://quotes.toscrape.com/'

    # Scrape quote authors with additional information
    quote_authors_info = scrape_quote_authors_info(url)

    # Display distinct quote authors with additional information
    print("Distinct Quote Authors with Additional Information:")
    for author in quote_authors_info:
        print(author)

if __name__ == "__main__":
    main()
