from train import PROGRESS
from typing import Mapping

from PIL.Image import register_save
import cv2
import os,time
import numpy as np

PROGRESS='Tight/'
# rice_tight: 60 , rice_sparse: 135

THRESHOLD = 60
testdir='test/'
ori_imgs_dir='/home/Rice/data/ori_imgs/train/' + PROGRESS
training_dir='/home/Rice/data/imgs/'+PROGRESS
masks_dir='/home/Rice/data/masks/'+ PROGRESS

# reverse 
# contour_dir='/home/Rice/data/contour/reverse/'
# reversed_dir='/home/Rice/data/masks/'
# resized_dir='/home/Rice/data/resized/'

# if not os.path.exists(contour_dir):
#     os.mkdir(contour_dir)
# if not os.path.exists(reversed_dir):
#     os.mkdir(reversed_dir)


def get_imgPath(fileName,dir):
    return dir+fileName

def rand_crop_img(img,CROP_N=10,resolution=512):
    H, W, C = img.shape

    for i in range(CROP_N):
        x1 = np.random.randint(W - resolution)
        y1 = np.random.randint(H - resolution)
        x2 = x1 + resolution
        y2 = y1 + resolution

        # https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
        crop_img=img[y1:y2,x1:x2]
        cv2.imwrite(training_dir+file.replace(".JPG","")+"_"+str(i+1)+".JPG",crop_img)

def find_contour():
    global THRESHOLD,PROGRESS
    imgs=os.listdir(training_dir)
    for file in imgs:
        img=cv2.imread(training_dir+file)   
        # height,width=img.shape[:2]
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
        ret, binary_img = cv2.threshold(gray,THRESHOLD,255,cv2.THRESH_BINARY)  
        contours, hierarchy = cv2.findContours(binary_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
        cv2.drawContours(img,contours,-1,(0,0,255),3)
        reversed_img=255-binary_img
        cv2.imwrite(masks_dir+file,reversed_img)

# def reverse_blake_white():
#     imgs=os.listdir(contour_dir)
#     for file in imgs:
#         print(file)
#         img=cv2.imread(contour_dir+file)
#         reversed_img=255-img
#         cv2.imwrite(masks_dir+file,reversed_img)
    

# def resize_imgs():
#     imgs=os.listdir(ori_imgs_dir)
#     masks=os.listdir(masks_dir)
#     for file in imgs:
#         img=cv2.imread(ori_imgs_dir+file)
#         img=cv2.resize(img,(3000,2000),interpolation=cv2.INTER_CUBIC)
#         cv2.imwrite(resized_dir+'train/'+file,img)
#     for file in masks:
#         img=cv2.imread(masks_dir+file)
#         img=cv2.resize(img,(3000,2000),interpolation=cv2.INTER_CUBIC)
#         cv2.imwrite(resized_dir+'mask/'+file,img)



if __name__ == '__main__':
    imgs=os.listdir(ori_imgs_dir)
    # crop img
    for file in imgs:
        print(file)
        path=get_imgPath(file,dir=ori_imgs_dir)
        img=cv2.imread(path)
        rand_crop_img(img, CROP_N=50, resolution=512)
    
    find_contour()
    # reverse_blake_white()
    # resize_imgs()
