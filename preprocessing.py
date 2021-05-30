from typing import Mapping

from PIL.Image import register_save
import cv2
import os

# find contour
imgs_dir='/home/Rice/data/imgs/train/' 
masks_dir='/home/Rice/data/masks/'

# reverse 
contour_dir='/home/Rice/data/contour/reverse/'
reversed_dir='/home/Rice/data/masks/'
resized_dir='/home/Rice/data/resized/'

if not os.path.exists(contour_dir):
    os.mkdir(contour_dir)
if not os.path.exists(reversed_dir):
    os.mkdir(reversed_dir)

def rand_crop_img_512():
    pass


def find_contour():
    imgs=os.listdir(imgs_dir)
    for file in imgs:
        img=cv2.imread(imgs_dir+file)   
        # height,width=img.shape[:2]
        # rice_sparse: 60 , rice_tight: 135
        THRESHOLD=135
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
        ret, binary = cv2.threshold(gray,THRESHOLD,255,cv2.THRESH_BINARY)  

        contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
        cv2.drawContours(img,contours,-1,(0,0,255),3) 
        cv2.imwrite(contour_dir+file,binary)

def reverse_blake_white():
    imgs=os.listdir(contour_dir)
    for file in imgs:
        print(file)
        img=cv2.imread(contour_dir+file)
        reversed_img=255-img
        cv2.imwrite(masks_dir+file,reversed_img)
    
def resize_imgs():
    imgs=os.listdir(imgs_dir)
    masks=os.listdir(masks_dir)
    for file in imgs:
        img=cv2.imread(imgs_dir+file)
        img=cv2.resize(img,(3000,2000),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(resized_dir+'train/'+file,img)
    for file in masks:
        img=cv2.imread(masks_dir+file)
        img=cv2.resize(img,(3000,2000),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(resized_dir+'mask/'+file,img)

## data augamentation
def random_crop_img():
    # calculate size  & range half a height, width
    # amount of imgs 

    pass

if __name__ == '__main__':
    rand_crop_img_512()
    # data_augmentation()
    # find_contour()
    # reverse_blake_white()
    resize_imgs()
