'''
Created on Dec 1, 2022

@author: Roger
'''
import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO

def getPlace():    
    with open('EncryptedGroupHints.json') as json_file:
        encrypt = json.load(json_file)
         
        # Print the type of data variable
        print("Type:", type(encrypt))
         
        # Print the data of dictionary
        print("\nReynolds:", encrypt['Reynolds'])
            
        # opening the file in read mode
        my_file = open("english.txt", "r")
          
        # reading the file
        data = my_file.read()
          
        # replacing end of line('/n') with ' ' and
        # splitting the text it further when '.' is seen.
        data_into_list = data.split("\n")
          
        # printing the data
        print(data_into_list)
        my_file.close()
        
        decoded_location = [data_into_list[int(x)] for x in encrypt['Reynolds']]
        print(decoded_location)
        
def load_groupPicture( filename ) :
    
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None