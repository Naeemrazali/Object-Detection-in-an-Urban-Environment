# Object-Detection-in-an-Urban-Environment
Udacity project one (computer vision)

https://github.com/Naeemrazali/Object-Detection-in-an-Urban-Environment

## Project Overview
Object detection is important for self-driving cars to be able to gain high level understanding of its environment from digital images captured from camera sensors. The car needs this information to be able to make optimal decisions such as at a stop sign or giving way to pedestrians at a zebra crossing. The aim of this project is to create a simple object detection model that can be used to identify cars, pedestrians, and cyclists from camera images.

# Dataset 

## Dataset Analysis
The dataset comes from the video feed of a camera attached to the front of a car. The dataset has images from a wide range of conditions. Weather conditions varied from sunny, cloudy and rainy. The camera was occasionally obscured by water droplets. Images were captured during the day and the night. Low light sensitivity of the camera sensor was poor, and reproduced a low amount of detail during night time scenes. The camera lense used did not have a wide FOV and lense distortion was minimal. Some scenes were void of any cars/pedestrians/cyclists. Other images were taken in the city with a high density of objects in the foreground and also background. Objects in the background would be of low resolution/blurry if size was too small. 

![Alt text](https://user-images.githubusercontent.com/38019946/141030902-4a5a30a8-4046-45a0-9384-ef38efc45db4.png?raw=true "Ten images extracted from dataset")

# Cross Validation 
The dataset consisted of 100 tfrecord files. To approximately distribute data equally over the different sets, the dataset was randomly shuffled. After shuffling the data was split into training, validation and testing sets. 70% of the files were used for training, 20% for validation and 10% for testing. 

10% of data was put into the testing set to check if the model is overfitting.

# Training 

## Reference Experiment
The training loss and validation loss graph is as below:

![Screenshot from 2021-11-15 20-59-21](https://user-images.githubusercontent.com/38019946/141743835-1f759182-8fd7-44fd-b61e-859b2c817e69.png)

The orange line represents the training loss, while the blue line represents the validation loss. Total loss for training and validation sets appear to converge. On closer inspection the values are 1.24 and 1.70 for training and validation loss respectively. Therefore, the model is slightly overfitting the training data. 

The precision and recall of the model is shown below:
![Screenshot from 2021-11-14 20-49-32](https://user-images.githubusercontent.com/38019946/141747672-18001c97-46f4-45bc-bb58-82c1591d8b7b.png)

![Screenshot from 2021-11-14 20-49-59](https://user-images.githubusercontent.com/38019946/141748418-37527f13-57d8-4c2c-a5fe-7cd72f8e032a.png)

The reference model precision and recall is represented by the dark blue line. The model precision and recall shows that it is still increasing. Which would mean that this model would benefit from having a larger dataset and increased steps for training.  


## Improvements Over Reference
 
Augmentations were applied to the model to increase the performance. Two augmentations were used in the model: random contrast and random black boxes. Contrast is chosen randomly from between 0.8 and 1.25. Contrast augmentation was chosen to introduce more lighting variance to the dataset. A maximum of 15 boxes with size to image ratio of 0.07 with probability of 0.5 was chosen. Adding random black patches to the dataset was done to increase performance of the model when given images that are obscured. 

Images of augmentations:

![output](https://user-images.githubusercontent.com/38019946/141760185-502d3662-8d04-434e-99cd-7da033a4acf3.png)

![output2](https://user-images.githubusercontent.com/38019946/141760196-9127f4b7-b44e-44db-9e18-d587ba2e64ef.png)

![output3](https://user-images.githubusercontent.com/38019946/141760218-24121ba1-4412-41d7-b3eb-1a877d5969df.png)


The learning rate of the model was decreased from 0.04 to 0.004. This was done to try to decrease model loss in the early stages of training (large initial loss). Warmup learning rate was also reduced to 0.0013333. Total number of steps was increased to 30000 from 25000 to try to increase the precision and recall of the model. 

Images of the improved model:
![Screenshot from 2021-11-15 20-58-35](https://user-images.githubusercontent.com/38019946/141743842-78d6684b-da77-4901-beb9-81fb2d064519.png)

Training loss is represented by the dark red line while validation loss is represented by the blue line. The loss is slightly lower compared to the reference model at 0.46 and 0.93 for the training and validation loss respectively. Some overfitting is still present in the improved model. 

The precision and recall of the model is shown below:
![Screenshot from 2021-11-14 20-49-32](https://user-images.githubusercontent.com/38019946/141747672-18001c97-46f4-45bc-bb58-82c1591d8b7b.png)

![Screenshot from 2021-11-14 20-49-59](https://user-images.githubusercontent.com/38019946/141748418-37527f13-57d8-4c2c-a5fe-7cd72f8e032a.png)

From the above graphs, the improved model is represented by the light blue line while the reference model is represented by the dark blue line. The precisong of the improved model increased across the board. Recall for the improved model was capped at 0.12 due max_number_of_boxes being limited to 12 in an attempt to reduce the amount of resources required for training the model. The improved model did increase in performance over the reference model in some recall metrics. 

The model performs well when presented with cars from a short to medium distance but struggles to identify cars from a long distance, and classifying pedestrians and cyclists. Improvements can be made by changing the model architecture to a more modern one and increasing training data for cyclists, pedestrians and cars from a distance
