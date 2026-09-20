import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IBM'

# Send an HTTP GET request to the webpage
headers = {
    "User-Agent": "MyLearningProject/1.0 (contact: kinshuk@yopmail.com)"
}
response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

# Store the HTML content in a variable
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')


with open("Assets/IBM.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# Display a snippet of the HTML content
# html_content[:500])