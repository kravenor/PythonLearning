import cv2
import numpy as np

img=cv2.imread('/home/kravenor/learning/PythonLearning/PythonOpenCV/Resources/lambo.jpg')
print(img.shape)

imgResize=cv2.resize(img,(300,200))
print(imgResize.shape)
imgCropped=img[0:200,200:500]

cv2.imshow('Lamborghini',img)
cv2.imshow('Resized',imgResize)
cv2.imshow('Croppeded',imgCropped)

cv2.waitKey(0)