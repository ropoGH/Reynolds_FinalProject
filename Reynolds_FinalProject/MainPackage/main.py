'''
Name: Roger Poduska
email: poduskrd@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Decrypts of code to show a selfie of group Reynolds in the designated place
Citations: N/a
Anything else that's relevant: N/a
'''
from FunctionPackage.functions import *
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO

#Retrieving the place to go for group picture
#See function for more info and documentation
getPlace()

#Capturing our image to show to screen
display_groupPicture("Reynolds_Photo.jpg")
