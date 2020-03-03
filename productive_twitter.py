#!/usr/bin/env python
# coding: utf-8



import tweepy
import sys
from PIL import Image
from os import walk
import psutil

def find_image(mypath):
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        return f

def kill_img():
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()


auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
api = tweepy.API(auth)




def add_image_to_tweet():
    while True:
        try:
            mypath = input('Path to Image Directory'+'\n')
            directory = find_image(mypath)
            len(directory)
        except TypeError:
            print('Not a Valid Folder Path'+'\n')
            continue
        else:
            img_dict = {k: v for k, v in enumerate(directory)}
            print('Image to Attach'+'\n')
            for k, v in img_dict.items():
                print(k,':',v)
            img = input()
            print(img_dict[int(img)]+' selected')
            view_img = Image.open(mypath+'/'+img_dict[int(img)])
            view_img.show()
            img_options = {0:'Yes', 1:'No'}
            while True:
                try:
                    confirm_img = int(input('Include This Image?'+'\n'+str(img_options)+'\n'))
                    img_confirmation = img_options[confirm_img]
                except (IndexError, ValueError):
                    print('Chose 0 for Yes or 1 for No')
                    continue
                else:
                    break
                if img_confirmation == 'Yes':
                    break
                else:
                    print('Returning to Image Selection Menu')
                    continue
            if img_confirmation == 'No':
                kill_img()
                continue
            else:
                break
            break
    kill_img()
    return mypath+'/'+img_dict[int(img)]




while True:
    try:
        message_body = input('Text Body'+'\n')
        link_to_tweet = input('Link to Send'+'\n')
        include_img_options = {0: 'Yes', 1: 'No'}
        include_img_options_selection = int(input('Include Image in Tweet?'+'\n'+str(include_img_options)+'\n'))
        if len(link_to_tweet) == 0:
            message = f"""{message_body}"""
        else:
            message = f"""{message_body}
{link_to_tweet}"""
        if include_img_options_selection == 1:
            None
            api.update_status(message)
        else:
            img_to_send = add_image_to_tweet()
            api.update_with_media(filename=img_to_send,status=message)
    except tweepy.TweepError as e: 
        print(e)
        continue
    else:
        break

