# Weed Detection for Agriculture 🌱

## Project Description

This project is a prove of concept for weed detection in agriculture. 

The model is trained on a collection of garden weed images from the [Weeds dataset](https://universe.roboflow.com/augmented-startups/weeds-nxe1w), making it capable of detecting weeds that typically blend in with their surroundings and confuse other detection models.


The tensorflow implementation of the Yolo model is taken and modified from the following repository:
https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3.git
🙌




## Dataset
Downlaod the data [Weeds dataset](https://universe.roboflow.com/augmented-startups/weeds-nxe1w) in COCO format and extract it to the data folder. You might need to adjust the paths in the config file.

## Training
To train the model run the following file:

`train.py`

## Inference
To run inference on a folder of .jpg images run the following file:
`detect_herbs.py`

You might need to adjust the weight the paths in the config file.

## Results
Some test set results after 5 epochs with 96.035% mAP:

<table>
<tr>
<td>
<img src="docu/20210907_153931_x264_mp4-81_jpg.rf.630b1b9f3450fe42f4906c765961011a.jpg" alt="Image 1" style="width: 90%;">
</td>
<td>
<img src="docu/20210907_153931_x264_mp4-213_jpg.rf.e63a8106d57153edb7a8075fd9887580.jpg" alt="Image 2" style="width: 90%;">
</td>
</tr>
<tr>
<td>
<img src="docu/20210907_153931_x264_mp4-255_jpg.rf.130ba437c7d6dc4376bcceca30b10293.jpg" alt="Image 3" style="width: 90%;">
</td>
<td>
<img src="docu/20210907_153931_x264_mp4-766_jpg.rf.5b1ed31e89d55788ec4354f18ca0410b.jpg" alt="Image 4" style="width: 90%;">
</td>
</tr>
<tr>
<td>
<img src="docu/20210907_153931_x264_mp4-847_jpg.rf.93123dbbdd3e9f74bf6c002d6a2d347f.jpg" alt="Image 5" style="width: 90%;">
</td>
<td>
<img src="docu/20210907_153931_x264_mp4-1581_jpg.rf.f4e344bbaeff32bfcf3de09d55058922.jpg" alt="Image 6" style="width: 90%;">
</td>
</tr>
<tr>
<td>
<img src="docu/20210907_153931_x264_mp4-1607_jpg.rf.dfcd4474e14f7917a6a9fb103298d24d.jpg" alt="Image 7" style="width: 90%;">
</td>
<td>
<img src="docu/20210907_153931_x264_mp4-1705_jpg.rf.013e4d21db5b043c1fa1aa9b54e59943.jpg" alt="Image 8" style="width: 90%;">
</td>
</tr>
</table>