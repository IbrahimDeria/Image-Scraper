import requests
from bs4 import BeautifulSoup
import urllib.request
import os

# User input for search query and number of images to download
search_query = input("What would you like to search for?")
num_images = int(input("How many images would you like to recieve?"))

# Create a directory to save downloaded images
if not os.path.exists(search_query):
    os.makedirs(search_query)

# Construct the Google search URL based on the search query
url = "https://www.google.com/search?q=" + \
    search_query + "&source=lnms&tbm=isch"

# Send a GET request to the URL and parse the HTML response using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all image tags in the HTML response
image_tags = soup.findAll("img")

# Download the first 'num_images' images to the directory
count = 0
for image_tag in image_tags:
    if count == num_images:
        break
    try:
        # Get the image URL from the 'src' attribute of the image tag
        image_url = image_tag['src']
        # Download the image and save it to the directory
        urllib.request.urlretrieve(image_url, os.path.join(
            search_query, search_query + "_" + str(count) + ".jpg"))
        print("Downloaded image ", count+1)
        count += 1
    except:
        pass

print("The images were downloaded in this folder: "+os.getcwd())
