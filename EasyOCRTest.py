
import re
import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import time
from langdetect import detect


#This is text recognition function return output text and accuracy
def recognition(IMAGE_PATH):
    try:
        # Initialize EasyOCR reader
        reader = easyocr.Reader(['kn'], gpu=False)  # Specify language (e.g., Kannada 'kn')
        
        # Perform OCR on the image
        result = reader.readtext(IMAGE_PATH)  # Detailed output with bounding boxes and confidence
        result_texts = reader.readtext(IMAGE_PATH, detail=0)  # Extract text-only
        
        # Calculate accuracy based on confidence scores
        confidence_scores = [res[2] for res in result if len(res) > 2]  # Extract confidence values
        accuracy = round(sum(confidence_scores) / len(confidence_scores) * 100, 2) if confidence_scores else 0.0

        # Combine all recognized texts into one string
        text = " ".join(result_texts)
    
        # Write recognized text to 'qw.txt'
        with open('qw.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        
        # Return only text and accuracy
        return text, accuracy
    
    except Exception as e:
        print(f"Error in recognition function: {e}")
        return "", 0.0
    
'''
#to recognize the text from
def recognition(IMAGE_PATH):

    reader = easyocr.Reader(['kn'], gpu=False)#kn ar
    result = reader.readtext(IMAGE_PATH)
    result1 = reader.readtext(IMAGE_PATH,detail=0)
    #print(result1)
    with open('qw.txt', 'w', encoding='utf-8') as f:
        f.write(str(result1))
        print(str(result1))
    
    confidence_scores = [res[2] for res in result if len(res) > 2]  # Extract confidence
    accuracy = round(sum(confidence_scores) / len(confidence_scores) * 100, 2) if confidence_scores else 0.0

    def listToString(s): 
        
        # initialize an empty string
        str1 = "" 
        
        # traverse in the string  
        for ele in s: 
            str1 += ele  
        
        # return string  
        return str1
    s11=''


    with open("qw.txt", "r",encoding='utf-8') as file:
        data1 = file.readlines()
        #print(data1)
        for line in data1:
            line=str(line)
            s=listToString(line)
            #print('s{}'.format(s))
            word = str(line.split())

    ln=detect(word)
    print('Language Detected {}'.format(ln))

    s = [float(s) for s in re.findall(r'-?\d+\.?\d*', word)]
    #print('Extracted Date {}'.format(s))

    def split(word):
        return [char for char in word]

    dd=split(s11)
    #print('dd {}'.format(dd))
    l=len(dd)
    l=int(1)

    top_left = tuple(result[0][0][0])
    bottom_right = tuple(result[0][0][2])
    text = result[0][1]
    font = cv2.FONT_HERSHEY_SIMPLEX

'''
