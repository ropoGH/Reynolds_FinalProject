'''
Name: Roger Poduska, Ben Marquis, Dana Garadah
email: poduskrd@mail.uc.edu, marquibm@mail.uc.edu, garadada@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Contains functions to decrypt hint and display our photo
Citations: N/a
Anything else that's relevant: N/a
'''
import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO
from fileinput import filename

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
        
def display_groupPicture( filename ) :
    
    try:
        myimage = Image.open(filename)
        myimage.load()
    except:
        return None
    
    myimage.show()



    
    