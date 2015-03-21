# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:05:27 2015

@author: Cole Gulino, Mohamed Shemy
"""
import sys
import cv2
import scipy as sc
import numpy as np

def showImage(image):
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cvtBandW(letter):
    bw_letter = []
    for i in xrange(0,20):
        for j in xrange(0,20):
            if letter[i,j] > 20:
                bw_letter.append(1)
            else:
                bw_letter.append(-1)
    return bw_letter

def hardlims(vector):
    for i in range(400):
        if vector[i] >= 0:
            vector[i] = 1
        else:
            vector[i] = -1
    return vector

#Let the user know that you are running the algorithm
print "========================================"
print "Starting Character Recognition algorithm"
print "========================================"

#Get the letter you want to run from the argument list of the command line
letter = " "
#Get the image name you want to test
letter_file = raw_input("Name of image file you want to test: ")

#Get image from file
try:
    image = cv2.imread(letter_file)
    showImage(image)
except:
    print "Error: Cannot find file"
    sys.exit()


#Turn the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
showImage(gray_image)

#Set the gray scale threshold for the image
(ret, th_image) = cv2.threshold(gray_image, 25, 255, 0)

#Find the contours
contours, hierarchy = cv2.findContours(th_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contour = contours[len(contours)-2]

#Find the x,y,width, and height of the contour around the letter
x,y,width,height = cv2.boundingRect(contour)

#create an image the size of the letter
letter = gray_image[y:y+height,x:x+width]
letter = cv2.resize(letter, (20,20))
showImage(letter)

#Convert image to black and white
bw_letter = cvtBandW(letter)
bw_letter = np.transpose(bw_letter)

#Get the weight matrix from the file
try:
    W = np.loadtxt('weight_matrix.txt')
except:
    print "Error: Cannont find file"
    sys.exit()

#multiply the wieght vector with the test matrix
result_vector = np.dot(W, bw_letter)
result_vector = hardlims(result_vector)
result_vector_t = result_vector.reshape((20,20))
showImage(result_vector_t)

#Open the dictionary of the ltters
try:
    dictionary = {}
    dictionary = open('dictionary.txt', 'r').read()
    dictionary = eval(dictionary)
except:
    print "Error: file cannot be read."

#Try to test characters for result in dictionary if they are close
print "========================================"
print "                Results                 "
print "========================================"
for char, vector in dictionary.items():
    count = 0
    if np.array_equal(result_vector, vector):
        print "The result for " + letter_file + " is: " + char
    else:
        for element in xrange(400):
            if result_vector[element] == vector[element]:
                count += 1
        if (float(count)/len(result_vector)) >= 0.80:
            print char, ": ", (float(count)/len(result_vector))*100, "%"
