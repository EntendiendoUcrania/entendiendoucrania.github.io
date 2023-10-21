import os
import datetime
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from dateutil.parser import parse
from urllib.parse import urljoin
import requests

# Define the URL of the index file
url = '_site/index.html'

# Send a GET request to the URL and parse the HTML using BeautifulSoup
with open(url, 'r', encoding='utf-8') as file:
    html = file.read()
soup = BeautifulSoup(html, 'html.parser')

# Define the metadata for the RSS feed
feed_title = 'Entendiendo Ucrania'
feed_link = 'https://entendiendoucrania.com/'
feed_description = 'Entendiendo Ucrania recoge artículos sobre la guerra, la sociedad y la historia de Ucrania escritos por sus protagonistas.'

# Create the root element of the XML
rss = ET.Element('rss', version='2.0')
channel = ET.SubElement(rss, 'channel')
ET.SubElement(channel, 'title').text = feed_title
ET.SubElement(channel, 'link').text = feed_link
ET.SubElement(channel, 'description').text = feed_description
ET.SubElement(channel, 'language').text = 'es'



# Find all the posts in the HTML and loop over them
posts = soup.find_all('div', class_='post')
for post in posts:
    # Extract the necessary information from the post
    post_link = post.a['href']
    post_date_str = post.find('span', class_='pubDate').text.strip()
    post_date_obj = parse(post_date_str)
    post_title = post.find('h2').text
    post_author = post.find('p', class_='author').text

    
# Find the post description
    post_description_elem = post.find('span', class_='descript')
    if post_description_elem:
        post_description = post_description_elem.text
    else:
        post_description = ""

# Find the post image
    post_image_elem = post.find('img')
    if post_image_elem:
        post_image_url = urljoin(url, post_image_elem['src'])
    else:
        post_image_url = None
    

# Create an item element for the post
    item = ET.SubElement(channel, 'item')
    ET.SubElement(item, 'title').text = post_title
    ET.SubElement(item, 'link').text = post_link
    ET.SubElement(item, 'description').text = post_description
    ET.SubElement(item, 'pubDate').text = post_date_obj.strftime('%a, %d %b %Y')
    ET.SubElement(item, 'author').text = post_author
    
    # Add the enclosure element if image URL is available
    if post_image_url:
        enclosure = ET.SubElement(item, 'enclosure', url=post_image_url, length='', type='image/webp')

# Create the XML tree and write it to a file
tree = ET.ElementTree(rss)
tree.write('entendiendoucrania.xml', encoding='utf-8', xml_declaration=True)

print(f"RSS feed successfully modified.")