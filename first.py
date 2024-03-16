import requests
from bs4 import BeautifulSoup

def scrape_book_details(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting book details
    book_name = soup.find('h1').text.strip()
    price = soup.find('p', class_='price_color').text.strip()
    stock_status = soup.find('p', class_='instock availability').text.strip()
    rating = soup.find('p', class_='star-rating')['class'][1]
    description = soup.find('meta', attrs={'name': 'description'})['content']
    product_info = soup.find('table', class_='table table-striped').find_all('td')[1].text.strip()
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()

    # Return a dictionary containing scraped details
    return {
        'Book Name': book_name,
        'Price': price,
        'Stock Status': stock_status,
        'Rating': rating,
        'Description': description,
        'Product Information': product_info,
        'Category': category
    }

if __name__ == "__main__":
    # URL of the book page you want to scrape
    url = 'https://books.toscrape.com/catalogue/the-black-maria_991/index.html'

    # Scrape book details
    book_details = scrape_book_details(url)

    # Print scraped details
    for key, value in book_details.items():
        print(f"{key}: {value}")
