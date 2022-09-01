# SnoringDetector
As part of the final project in my master's degree in electrical engineering I developed a snore detector.

![alt text](https://www.raleighcapitolent.com/wp-content/uploads/2021/09/how-to-stop-snoring.jpg)

The initial step was to build a system that would detect when there is snoring and count the number of snoring for an allotted time.

<strong>The steps to build the model:</strong>

1.The first step is finding the data. Data of snoring is not very common. But there is a pretty good dataset source on the kaggle website.
The address of the dataset: https://www.kaggle.com/datasets/tareqkhanemu/snoring

2.The next step was to find a model suitable for binary classification (either there is snoring or there is not). I took the basis of my model from a video that helped me make detectors of special birds, its address: https://www.youtube.com/watch?v=ZLIPkmmDJAc&list=LL&index=4

3.After I trained and found a model that satisfies in terms of results. I saved it so I could load it later without the training phase. 

4.The next step was to build a UI (the simplest one - just see if the machine works) and actually take data in real time and cut it into slices of one second back in time and give a result whether this second is snoring or not snoring.


<strong>Running the program:</strong>

1.Downloading the data to the local computer.The folder will be named "Snoring_Dataset".
The address of the dataset: https://www.kaggle.com/datasets/tareqkhanemu/snoring
You can create a folder of pre-recorded audio and test the model. The audio will be in the "Test_Data" folder.

2.Running the file Model_development.ipynb (preferably in a notebook) and saving the model (my_h5_model.h5 in "saved_models" folder)

3.The last step is to run the main.py function. This function loads the model and then enters a 20 second loop of recording the audio to mp3 one second back. Then switch to a wav file with a sampling frequency of 16K as we trained the model.
The model then predicts whether that slice is 1 or 0 (snoring or not snoring). All this happens in real time with a fairly simple UI.


This program is an initial stage, so I would appreciate feedback and improvement: Oranne5@gmail.com

Here I present the working program. Because it's a GIF it can't be heard but believe me while it was showing snoring I made a snoring sound:
![](https://github.com/orannahum/SnoringDetector/blob/main/snoring%20detection.gif?raw=true)
