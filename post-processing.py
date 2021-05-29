from typing import Mapping
from typing_extensions import Concatenate
from PIL.Image import register_save
import cv2
import os
import pandas

predicted_dir='output/'
submit_dir='submit/'

if not os.path.exists(submit_dir):
    os.mkdir(submit_dir)

def crop_img():
    # crop into 4 imgs

    pass

def find_center():
    imgs=os.listdir(predicted_dir)
    for file in imgs:
        path=predicted_dir+file
        img=cv2.imread(path)
    
    # output points to csv file



def concatenate_masks():
    # concatenate 4 imgs

    pass



def output_csv():
    pass

if __name__ == '__main__' :
    crop_img()
    find_center()
    concatenate_masks()
    output_csv()
