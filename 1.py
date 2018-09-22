from __future__ import print_function
import tweepy
import os
from tweepy import OAuthHandler
import json
import wget
import argparse
import configparser
import glob
import sys
import subprocess
import io
import requests
from google.cloud import vision
from google.cloud.vision import types
from google.auth import app_engine
#your twitter credentials
consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_secret = ' '
 
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
#taylorswift13 here is a twitter account
tweets = api.user_timeline(screen_name='taylorswift13',
                           count=200, include_rts=False,
                           exclude_replies=True)
last_id = tweets[-1].id
 
while (True):
	more_tweets = api.user_timeline(screen_name='taylorswift13',
                                include_rts=False,
                                exclude_replies=True,
                                max_id=last_id-1)
# There are no more tweets
	if (len(more_tweets) == 0): 
		break
	else:
		last_id = more_tweets[-1].id-1
		tweets = tweets + more_tweets

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])      

for media_file in media_files:
    wget.download(media_file)        

##Rename photo by num for ffmpeg
def order():
    i=1
    path=" path"## change to local path
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            os.rename(path + "/" + filename, path + "/" + str(i) + ".jpg")
            i+=1

##Error checking for pictures in selected folder 
def checkError():
    os.chdir(" path ") ## change to local path
    if (glob.glob("*.jpg")) == []:
        sys.exit('Error: Please carefully re-enter twitter credentials and rerun.')


  
##ffmpeg tool for video creation
def video():
    subprocess.call('ffmpeg -r .5 -f image2 -s 1920x1080 -i %d.jpg -vcodec libx264 -crf 20  -pix_fmt yuv420p test.mp4', shell=True)
    print('\n\nVideo created.')

def createLabels():
	client = vision.ImageAnnotatorClient()
	
    # create file 
	f1 = open('new.txt','w+') 
	f1.write('Labels:')

    # The name of the image file to annotate
	directory =  "path"  ## change to local path
    #for i in range(1,n):
	for filename in os.listdir(directory): 
		if filename.endswith(".jpg"):
			file_name = filename 
                # Loads the image into memory 
			with io.open(file_name, 'rb') as image_file:
				content = image_file.read()
				image = types.Image(content=content)

            # Performs label detection on the image file
			response = client.label_detection(image=image)
			labels = response.label_annotations

			for label in labels:
				f1.write('\n')  
				f1.write(label.description)
                #labels created in new.txt
                

	f1.close()

def main():
    order()
    checkError()
    video()
    createLabels()


if __name__=='__main__':
	main()    