# Sign-Language-Recogntion-System

# About Project
![image](https://user-images.githubusercontent.com/21967832/208241394-fec2887e-a836-4916-98c6-2635bf6f24d2.png)


# Methodology
![image](https://user-images.githubusercontent.com/21967832/208241391-a36ec4e4-9e72-49ae-aba2-ae71be4dc7c4.png)

The proposed methodology uses the Neural Network approach along with Mediapipe for sign language recognition.
Dataset Generation – We have selected the ASL alphabet dataset on Kaggle to be used in this project without the signs of “nothing” and “delete”. Initially the whole dataset downloaded in directory is passed to mediapipe for detection of hand landmarks.
Data Preprocessing - These landmark points are concatenated in numpy arrays which are further appended in an empty list that makes up the whole data to be used for training. The labels are concurrently encoded during this process for each feature , that is for landmarks for each frame.
Training – The dataset produced from the previous stage is trained on a custom made LSTM model and the weights of the model are saved for testing in the application. 
Testing - Initially the frame is captured from the video and passed to Mediapipe. Mediapipe framework then detects hands from the frames and uses CNN to map 3D coordinates (x, y , z) onto it. The coordinates(landmarks) are extracted and appended to a numpy array. The processed dataset is tested using saved weights .
Final Product:-Tkniter is used to develop the GUI for the deliverable software application.


# Description
Dataset used - ASL alphabet on Kaggle - https://www.kaggle.com/datasets/grassknoted/asl-alphabet
Number of classes - 27 (A-Z and Space)
Number of images - 89000
Model Used - LSTM
Accuracy - 95%


# Input/Output

![image](https://user-images.githubusercontent.com/21967832/208241457-c417a943-fd49-4a9a-8b60-feda944741bf.png)
System predicting sign "I" of ASL.

![image](https://user-images.githubusercontent.com/21967832/208241438-d0aeef30-3268-4918-9b9c-7c68a5bc73ce.png)
System predicting sign "C" of ASL.


![image](https://user-images.githubusercontent.com/21967832/208241480-d878e452-147a-4bf0-8c2f-3257a14de5d3.png)


# Live Link
The project isn't hosted online but it is in the form of a executable software file developed using tkinter.

# Installation

Dowload Zip Code.
Open terminal in folder and use command - pip install -r requirements.txt
run command - python main.py


# ScreenShot of The Interface
![image](https://user-images.githubusercontent.com/21967832/208241497-ea531730-8508-44aa-9604-24cdf87246fd.png)

![image](https://user-images.githubusercontent.com/21967832/208241502-0e5780b7-f05d-459f-ba63-4e6f521e7ff5.png)

![image](https://user-images.githubusercontent.com/21967832/208241508-0ca0ebe2-149b-4b57-bd52-387015c8304d.png)

System predicting Sign "I" of ASL.

