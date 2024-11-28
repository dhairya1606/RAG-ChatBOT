import requests
from bs4 import BeautifulSoup

def extract_text_from_web(url):
    # Send an HTTP request to get the webpage content
    response = requests.get(url)
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tags_to_avoid = [
        "script", "style", "header", "footer", "nav", 
        "aside", "form", "button", "iframe", "noscript", 
        "input", "select", "option", "link", "meta", 
        "img", "video", "audio", "advertising", "noscript"
    ]

    # Remove script, style, and other irrelevant tags
    for script in soup(tags_to_avoid):
        script.extract()  # Remove these tags from the soup
    
    # Extract the article body by identifying important sections
    text = ''
    
    # Try to find the main content
    if soup.body:
        # Finding the main content, usually within <article>, <div> tags with relevant class
        article = soup.find_all(['article', 'div', 'section', 'p'])
        for section in article:
            text += section.get_text(separator=" ", strip=True) + " "

    # Clean the text further, remove excess whitespace
    cleaned_text = ' '.join(text.split())
    
    return cleaned_text

# Example URL to extract text from
# url = 'https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/'
# extracted_text = extract_text_from_web(url)

# with open("web_text.txt", 'w') as f:
#     f.write(extracted_text)

# # Display the extracted text
# print(len(extracted_text))
