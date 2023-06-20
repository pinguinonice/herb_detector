import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model, detect_video_realtime_mp
from yolov3.configs import *
import random

if TRAIN_ON_M1 == True:
        tf.config.set_visible_devices([], 'GPU')

else:
    gpus = tf.config.experimental.list_physical_devices('GPU')
    print(f'GPUs {gpus}')
    if len(gpus) > 0:
        try: tf.config.experimental.set_memory_growth(gpus[0], True)
        except RuntimeError: pass



image_folder = "dataset/Weeds.v3-augmented_nottrained.yolokeras/test/"


yolo = Load_Yolo_model()



    
#detect_image(yolo, image_path, "pcb_prediction.jpg", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))

# jpg files in image_folder, predict and save in output_folder
filenames = os.listdir(image_folder)
#remove non-jpg files
for filename in filenames:
    if not filename.endswith(".jpg"):
        filenames.remove(filename)

random.shuffle(filenames)
for filename in filenames:

    image_path = os.path.join(image_folder, filename)
    print(image_path)
    image,pred_bbox_org=detect_image(yolo, image_path, os.path.join('dataset/Weeds.v3-augmented_nottrained.yolokeras/predictions/', filename), input_size=YOLO_INPUT_SIZE, show=False, CLASSES=TRAIN_CLASSES, score_threshold=0.5, iou_threshold=0.45, rectangle_colors=(255,0,0))

    # save image with bounding boxes
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    cv2.imwrite('dataset/Weeds.v3-augmented_nottrained.yolokeras/predictions/'+filename, image)    
