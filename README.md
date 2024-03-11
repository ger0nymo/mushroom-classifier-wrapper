# Mushroom Classifier

## Introduction:
Embarking on a college project, I found inspiration in a mushroom image dataset while exploring public Kaggle datasets. The challenge was intriguing: to classify mushrooms using machine learning. Armed with Google Colab Premium's robust GPU support, including Tesla T4 and NVIDIA A100, I aimed to expedite the training process for my models, which proved to be immensely beneficial.

## Dataset Exploration:
The dataset, comprising around 7000 labeled images, initially posed a challenge as it was formatted for object detection. To make it suitable for training classification models, I converted it by utilizing the COCO-formatted JSON. This involved creating subdirectories for 21 mushroom genera, each containing the relevant images. 
After converting it to the correct format, I resplit them so that 85% of the images would be used for training purposes, leaving 15% for validation or testing.

## Model Training Attempts:
With minimal machine learning knowledge, I delved into object detection and classification. My first attempt involved building a custom model using TensorFlow. Although the process was straightforward, the model's output yielded only a 40% accuracy on the validation dataset, far from satisfactory for this project's standards.

## Shift to Existing Models:
Undeterred, I shifted my focus to existing classification models. Detectron2, an initial choice, faced dependency version conflicts on Colab, prompting me to explore alternatives. The contenders were EfficientNetV2 and YOLOv8. While EfficientNetV2 reached a 70% accuracy, YOLOv8 outperformed it with a top1 accuracy of 90% and a top5 accuracy exceeding 98% on the validation dataset.

## Model Implementation and Backend Development:
Having chosen YOLOv8 for its superior performance, the next step was implementing the trained model. I opted for Flask, a Python-based backend technology, to set up an HTTP endpoint. This endpoint receives image inputs from a frontend, runs predictions using the model, and sends the results back to the client. The backend's simplicity and compatibility made it an ideal choice for seamless integration.

## Frontend Development:
To complement the backend, I designed a mobile app for user convenience. Leveraging my prior experience, I chose Flutter for its cross-platform capabilities. Utilizing BLoC state management, I crafted a clean and sophisticated user interface. The mobile app enables users to capture images, sending them to the backend for predictions through the trained model.

## Conclusion:
In summary, the mushroom classifier project has reached its conclusion with the integration of the Flutter app. Users can easily capture images through the mobile app and receive accurate-enough predictions from the trained model. Although not intended for production use, the attained accuracy makes it able to see the goal of the project.

## Subproject-repositories:
* YOLOv8 model training: https://colab.research.google.com/drive/1ipBfcB8x8-KU1yH657FNenfYG_HH29Z8
* Flask backend: https://github.com/ger0nymo/mushroom-classifier-backend
* Flutter frontend: https://github.com/ger0nymo/mushroom-classifier-frontend

### Resources:
* Tensorflow: https://www.tensorflow.org/
* Dataset: https://universe.roboflow.com/mushroom28/mushroom-nksu4/dataset/6
* YOLOv8 documentation: https://github.com/ultralytics/ultralytics
