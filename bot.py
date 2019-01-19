from urllib.request import urlopen
from urllib import parse
from time import sleep
import datetime
import praw
import logging

print("Started DankMemes bot 8000")

# turns out logging is broken so ignore this
logging.basicConfig(filename='output.log',level=logging.DEBUG)
logging.info('Started Dankmemes bot 8000')
all_urls = []

def reddit_call():
    reddit = praw.Reddit(client_id = 'REDDIT CLIENT ID',
                     client_secret = 'REDDIT CLIENT SECRET',
                     username='REDDIT USERNAME',
                     password='REDDIT PASSWORD',
                     user_agent='meme_bot_8000')

    subreddit = reddit.subreddit('dankmemes')

    hot_python = subreddit.hot(limit=10)

    acceptable = []
    global all_urls

    # Go through the top 5, and exclude any that arent pictures
    # of the right format or are stickied
    for submission in hot_python:
        if not submission.stickied:
            link = submission.url
            title = submission.title
            if link[-4:].lower() in ['.jpg','.png']:
                if 'mods' not in title and 'reddit' not in title:
                    if link not in all_urls:
                        acceptable.append(link + '&img_msg=' + title)
                        all_urls.append(link)

    # Pick the top one by default
    return acceptable[0]

# Testing url:
# https://i.redditmedia.com/Xrmi691_AA00WqLN95cmPHd7inYBIwlkQJql0ruTbMk.jpg?w=793&s=a3867273e912ae2df4cd25a11cb03944

last_hour = 0

times = [[3, 21],       # Monday        3am, 9pm
         [3, 21],       # Tuesday       3am, 9pm
         [3, 21],       # Wednesday     3am, 9pm
         [3, 21],       # Thursday      3am, 9pm
         [3, 15, 21],   # Friday        3am, 3pm, 9pm
         [3, 15, 21],   # Saturday      3am, 3pm, 9pm
         [3, 15, 21]]   # Sunday        3am, 3pm, 9pm

while True:
    current_time = datetime.datetime.now()
    
    if last_hour != current_time.hour:
        # New hour, check if it's in the list for this day of the week
        
        if current_time.hour in times[current_time.weekday()]:
            # Good to execute code!
            print("Making post")
            logging.info("Making Post: " + str(current_time.date()) + ' ' + str(current_time.time()))

            # Get url from reddit API
            url = reddit_call()

            print("URL to parse: " + url)
            logging.info("URL to parse: " + url)
            
            url_query = 'URL TO PHP SCRIPT GOES HERE ?img_url=' + parse.quote_plus(url, '&=')

            print("URL Query: " + url_query)
            logging.info("URL Query: " + url_query)

            result = urlopen(url_query)

            data = result.read()

            print("Data Decode: " + data.decode())
            logging.info("Data Decode: " + data.decode())
        else:
            print("Not time yet")
            logging.info("Not time yet")
            
        last_hour = current_time.hour
    else:
        print("Not time yet, wait for later")
        logging.info("Not time yet, wait for later")

    # Delay for a minute
    sleep(60)

    
