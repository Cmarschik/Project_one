import oauth2
import constants
import urllib.parse as urlparse

consumer = oauth2.Consumer(constants.CONSUMER_SECRET, constants.CONSUMER_SECRET)

def get_request_token():
    

