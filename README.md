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
Some results after only 3 epochs:

<table style="width:90%">
  <tr>
    <td><img src='docu/20210907_153931_x264_mp4-184_jpg.rf.d84795ffcfda403b97a022567dc0cde6.jpg' alt='Image 1' /></td>
    <td><img src='docu/20210907_153931_x264_mp4-216_jpg.rf.ee70431461177dde38b01a476581acc7.jpg' alt='Image 2' /></td>
  </tr>
  <tr>
    <td><img src='docu/20210907_153931_x264_mp4-412_jpg.rf.89b20d28da734856679cc8276d45d779.jpg' alt='Image 3' /></td>
    <td><img src='docu/20210907_153931_x264_mp4-579_jpg.rf.fc860e18b9860897eb95cba11c6850d3.jpg' alt='Image 4' /></td>
  </tr>
  <tr>
    <td><img src='docu/20210907_153931_x264_mp4-633_jpg.rf.fd1efb3a32553d54fb3cc88ad8804013.jpg' alt='Image 5' /></td>
    <td><img src='docu/20210907_153931_x264_mp4-915_jpg.rf.f20b07a8d61d13661d8a97a9a8ae15cf.jpg' alt='Image 6' /></td>
  </tr>
  <tr>
    <td><img src='docu/20210907_153931_x264_mp4-1140_jpg.rf.ff67b49559d09b679e891ee6cc4c8aed.jpg' alt='Image 7' /></td>
    <td><img src='docu/20210907_153931_x264_mp4-1723_jpg.rf.145e6211848adbf19e92919618b80954.jpg' alt='Image 8' /></td>
  </tr>
</table>