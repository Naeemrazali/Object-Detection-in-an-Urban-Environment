# Object-Detection-in-an-Urban-Environment
Udacity project one (computer vision)

## Project Overview
Object detection is important for self-driving cars to be able to gain high level understanding of its environment from digital images captured from camera sensors. The car needs this information to be able to make optimal decisions such as at a stop sign or giving way to pedestrians at a zebra crossing. The aim of this project is to create a simple object detection model that can be used to identify cars, pedestrians, and cyclists from camera images.

# Dataset 

## Dataset Analysis
The dataset comes from the video feed of a camera attached to the front of a car. The dataset has images from a wide range of conditions. Weather conditions varied from sunny, cloudy and rainy. The camera was occasionally obscured by water droplets. Images were captured during the day and the night. Low light sensitivity of the camera sensor was poor, and reproduced a low amount of detail during night time scenes. The camera lense used did not have a wide FOV and lense distortion was minimal. Some scenes were void of any cars/pedestrians/cyclists. Other images were taken in the city with a high density of objects in the foreground and also background. Objects in the background would be of low resolution/blurry if size was too small. 

![Alt text](https://user-images.githubusercontent.com/38019946/141030902-4a5a30a8-4046-45a0-9384-ef38efc45db4.png?raw=true "Ten images extracted from dataset")

# Cross Validation 
The dataset had a total of 100 tfrecord files. To approximately distribute data equally over the different sets, the dataset was randomly shuffled. After shuffling the data was split into training, validation and testing sets. 70% of the files were used for training, 20% for validation and 10% for testing. 

10% of data was put into the testing set to check if the model is overfitting.

# Training 

## Reference Experiment
This section should detail the results of the reference experiment. It should include training metrics and a detailed explanation of the algorithm's performance. 

The reference experiment used resnet-50 model without augmentations. 

Initially the model was overfitting as the training loss was diverging from the validation loss. The training loss is indicated in orange and the validation loss is in blue. This divergence indicates a significant error rate during model validation - an indication that the model is overfitting. The precision and recall curves indicate that the performance of the model slowly increases, as both precision and recall start to increase. A high recall rate is often not suitable and the model performance is not that great.  

## Improvements Over Reference
 This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
 
 To improve on the model performance, the first step was to augment the images by converting them to grayscale with a probability of 0.2. After this, we have clamped contrast values between 0.6 and 1.0 such that more ligthing datapoints are available for classification. A greater part of the images were a bit darker and increasing the brightness to 0.3 provided an even datapoint which could be better classfied with the model. The pipeline changes are there ine pipeline_new.config
 
 Augmentations applied:
 * Augmentation
 * Augmentation 

Images of augmentations

Images of the improved model

The loss is lower than the previous loss (un-augmented model). This is an indication of better performance. There should be more samples of augmented datapoints such as combining the caontrtast values with grayscale. Brightness can also be clamped within a limit instead of fixing it to 0.3. However, the most important point is to add more samples of cyclists, pedestrians which are in low quantity in the dataset. This is an inherent requirement since model biases play an important role in the loss curves and lesser the diversity in training samples, the lower will be the accuracy. 

We have reduced overfitting to an extent with augmentations, however better classification results would be resulting from a more balanced dataset. 


