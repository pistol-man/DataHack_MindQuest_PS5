import requests
from bs4 import BeautifulSoup

# Function to scrape a single custom URL and extract the content of a specific div
def scrape_single_url_and_extract_div(url, div_class):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad requests (4xx or 5xx status codes)
        
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the <div> element by its class name
        div_element = soup.find('div', class_=div_class)
        
        if div_element:
            # Extract and print the content of the div
            div_content = div_element.get_text() 
            # print("Content of the div:", div_content)
           
           
            words= div_content.split()
            
            div_content_string = ' '.join(words)
            print(div_content_string)    

        else:
            print("Div element with class", div_class, "not found on the page.")
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve the web page:", e)

# Input your custom URL and the class name of the div to extract content from
username="bypranavpawar"
url = "https://fueler.io/"+username
div_class = ("user-skills")

scrape_single_url_and_extract_div(url, div_class)
