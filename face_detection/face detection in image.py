# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:44:03 2021

@author: Dell
"""

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier("D:/Face Detection\haarcascade_frontalface_default.xml")

# Read the input image
img = cv2.imread("D:/Face Detection/test.jpg")

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('image', img)
cv2.waitKey()
