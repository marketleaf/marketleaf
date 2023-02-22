import random
import time
from instagrapi import Client
from numpy import random
from time import sleep
from instagrapi.exceptions import (
    UnknownError, ClientError
    )
import json       



#start time function
def starter():
    t = time.localtime()
    current_time_start = time.strftime("%H:%M:%S", t)
    print(f"Start of session at: {current_time_start}")

#end time function
def finisher():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"Finished session at:{current_time}")
    client.dump_settings("pyramid.json")

# sleep time functin
def sleeper():
    sleeptime = random.randint(6, 23)
    print("sleeping for:", sleeptime, "seconds")
    sleep(sleeptime)   

starter()

#Log In
username =
password =  
client = Client()

#load cookies


client.load_settings('market.json')
#client.dump_settings("market.json")


client.login(username, password)


print("Logged In")

sleeper()


#Hashtags
hashtags = ["socialmediatools", "digitalmarketer", "contentmarketing", "smallbusinessowners","marketingmotivation", "marketingtips", "brandingdesign" "webdesignagency" "businessmotivation","successmindset","uxdesign", "webdesign" , "seomarketing"]

hashtag = random.choice(hashtags)													

#Liking hashtags
medias = client.hashtag_medias_recent(hashtag, 8)
print("startofliking")

for i, media in enumerate(medias):
    try:
        client.media_like(media.id)
    except UnknownError:
        print("Exception UnknownError occured")
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(f"Marketleaf - Liked post number {i+1} of hashtag {hashtag} at time: {current_time}")
        sleeper()

#dumpsettings
#client.dump_settings("market.json")

finisher()