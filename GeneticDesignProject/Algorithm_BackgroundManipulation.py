import cv2 
import numpy as np 
from matplotlib import pyplot as plt

# This algorithm will use gamma to dim the background
def GammaCorrection(image=None, gamma=2.5):
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv2.LUT(image, lookUpTable)
    return (res)

# Determine the gamma level with histogram 
def whatsGamma(img_source = None):
    plt.hist(img_source.ravel(),256,[0,256])
    histr = cv2.calcHist([img_source], [0], None, [256], [0,256]) #Channel set to 0 for Grayscale image

    dark = np.average(histr[:127]) # Dark color area
    light = np.average(histr[127:]) # Bright color area
    ave = np.average(histr) #Average of the histogram, the number should be fixed based on the image resolution
    gamma = ((ave+light)/ave)+0.5   # This is trial and error algorithm, change if there is a better algorithm
    print('Gamma changer algorithm...')
    print('dark = ', dark)
    print('light = ', light)
    # print('ave = ', ave)
    print('gamma = ', gamma)
    # print(np.argmax(histr), histr[np.argmax(histr)])
    # print(np.argmin(histr), histr[np.argmin(histr)])
    # print(np.max(histr),
    #         histr[np.max(histr)])
    # print(np.min(histr),
    #         histr[np.min(histr)])
    # print(np.average(histr))
    # print()
    # Return the gamma level to be used in gamma correction algorithm
    return gamma
    # plt.show()