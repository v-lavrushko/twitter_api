import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def twit_dict(acct):
    '''
    (str) -> dict
    Creates dictionary from json file given by Twitter API
    '''
    assert (len(acct) >= 1), 'Name is not valid'
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '20'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    return js

def dict_info(old_dict):
    '''
    (dict) -> dict
    Filters dictionary and returns new dictionary with usefull information
    '''
    new_dict = {}
    users = old_dict['users']
    for line in users:
        info = [line['location'], line['url'], line['description'],\
                line['friends_count'], line['followers_count'],\
                line['profile_image_url']]
        new_dict.update({line['screen_name'] : info})
    return new_dict
