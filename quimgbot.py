# Tweet Quotes from Yaml
# Adapted from: https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, yaml, random, os

# Get environment variables (stored encrypted in github repository, and called into the OS from the action workflow file main.yml)
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

files=os.listdir('imgs')
img=random.choice(files)
img = 'imgs/' + img


media = api.media_upload(img)

hash = "#NonviolentCommunication #NVC #MarshallRosenberg"

api.update_status(status=hash, media_ids=[media.media_id])
