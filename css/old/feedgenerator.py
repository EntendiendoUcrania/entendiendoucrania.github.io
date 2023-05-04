import os
import smtplib
import schedule
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from feedgen.feed import FeedGenerator

# read the HTML file and extract the relevant information
with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

new_posts = []
for post in soup.find_all('div', {'class': 'post'}):
    post_date = datetime.strptime(post.find('span', {'class': 'date'}).text, '%Y-%m-%d')
    if post_date > datetime.now() - timedelta(days=15):
        post_title = post.find('h2', {'class': 'title'}).text
        post_link = post.find('a')['href']
        post_desc = post.find('p', {'class': 'description'}).text
        new_posts.append({'title': post_title, 'link': post_link, 'description': post_desc})

# check if there are any new posts
if new_posts:
    # check when the last email was sent
    last_email_file = 'last_email.txt'
    if os.path.isfile(last_email_file):
        with open(last_email_file, 'r') as f:
            last_email_date = datetime.strptime(f.read(), '%Y-%m-%d')
    else:
        last_email_date = datetime.now() - timedelta(days=15)

    # create the RSS feed with the new posts
    fg = FeedGenerator()
    fg.title('My News Website')
    fg.link(href='http://example.com', rel='alternate')
    fg.description('Updates on my news website')
    for post in new_posts:
        fe = fg.add_entry()
        fe.title(post['title'])
        fe.link(href=post['link'])
        fe.description(post['description'])
        fe.pubDate(datetime.now())

    # generate the RSS feed and write it to a file
    rss_file = 'my_news.rss'
    with open(rss_file, 'wb') as f:
        f.write(fg.rss_str(pretty=True).encode())

    # send the email to all subscribers
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('your_email@gmail.com', 'your_password')
        for subscriber in subscribers:
            message = f'Subject: New posts on my website\n\n'
            for post in new_posts:
                message += f'{post["title"]}\n{post["description"]
