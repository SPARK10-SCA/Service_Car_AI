# Service Car AI
## Hybrid Deep Learning and Machine Learning Approach for Car Damage Assessment and Repair Cost Prediction

![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


---
## Project Overview![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)
This repository contains the source code for the project 'Service Car AI'.
This project proposes and implements a following pipeline to assess car damage and predict repair costs based on a single damaged car image. 

<img src="https://user-images.githubusercontent.com/96368116/233840587-b6f5c194-b1bc-496c-8b63-c42088c78045.jpeg">

---
## Pipeline 🖇️
### Model 1. Car Part Segmentation
YOLOv8 Segmentation: The car parts (bumper, fender, etc) and the area of damage is segmented. Damaged car parts are then identified and cropped, which are then passed to the next models 2 and 3.
### Model 2. Car Damage Segmentation
U-Net Segmentation: Given damaged car parts, this model re-segments the damage into four categories: Breakage, Crushed, Scratched, Separated.
### Model 3: Repair Method Classification
VGG-19 Classification: Given damaged car parts, this model predicts the appropriate repair method from six categories.
### Model 4: Repair Cost Estimation
Gradient Boosting Regressor: This machine learning model predicts the repair cost of a damaged car part, given the output value of Model 3 and the basic information of the damaged car.

The final output aggregates the output of each model, assessing car damage and predicting the total estimated repair cost of the damaged car. This output, together with segmented images with damage, is presented visually through our web or app platform. 

---
## Achievements 🏅
- 2022 Co-Deep Learning Project 우수상
- 2023 S-TOP 우수상
- 2023 S-TOP 인기상
- 2022 SPARK Project

---
## Contributors 🙌 
- 송현빈 (성균관대학교 소프트웨어학과 20학번)
- 박민지 (성균관대학교 소프트웨어학과 21학번)
- 박성완 (성균관대학교 소프트웨어학과 20학번)
- 신상윤 (성균관대학교 소프트웨어학과 21학번)