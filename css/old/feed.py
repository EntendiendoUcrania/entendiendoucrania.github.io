import os
import datetime
import feedgenerator
from bs4 import BeautifulSoup
from dateutil.parser import parse
import requests

# Define the URL of the index file
url = 'https://entendiendoucrania.com/index.html'

# Send a GET request to the URL and parse the HTML using BeautifulSoup
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

# Define the metadata for the RSS feed
feed_title = 'Entendiendo Ucrania'
feed_link = 'https://entendiendoucrania.com/'
feed_description = 'Entendiendo Ucrania recoge artículos sobre la guerra, la sociedad y la historia de Ucrania escritos por sus protagonistas.'

# Create a FeedGenerator object and set its metadata
feed = feedgenerator.Rss201rev2Feed(
    title=feed_title,
    link=feed_link,
    description=feed_description,
    language='es',
)


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
    

    post_image_elem = post.find('img')
    if post_image_elem:
        post_image_url = post_image_elem['src']
        post_image_title = post_image_elem['alt']
        post_image_link = post_image_elem.parent['href'] if post_image_elem.parent.name == 'a' else post_link
        post_image_size = os.path.getsize(post_image_url)
        post_image_type = 'image/webp'  # Change to the appropriate MIME type for the image
        post_image_data = requests.get(post_image_url).content

        # Add an enclosure for the image to the RSS item
        feed.add_item(
            title=post_title,
            link=post_link,
            description=post_description,
            pubdate=post_date_obj,
            author=post_author,
            enclosure=(post_image_url, post_image_size, post_image_type, post_image_title),
        )

    else:    

# Create an entry for the post in the RSS feed
        feed.add_item(
            title=post_title,
            link=post_link,
            description=post_description,
            pubdate=post_date_obj,
            author_name=post_author,
        )
    

# Generate the RSS feed and write it to a file
rss_feed = feed.writeString('utf-8')
with open('entendiendoucrania.xml', 'wb') as f:
    f.write(rss_feed.encode('utf-8'))
