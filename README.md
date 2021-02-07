# Rating and Participation Prediction Web App
## Data Mining Project
Predicting score ratings using CPD Analysis Dataset.

## Table of Contents
* Problem Understanding
* Dataset Description
* Hypothesis from Dataset
* Stakeholders
* Exploratory data analysis steps
* Data Preprocessing 
* Descriptive and Predictive Data Mining
* Data Mining Performances Comparison
* Conclusion
* Reflection

## Problem Statement
From the CPD analysis, I found out the rating score given by the participants and number of participants in 2020 does not achieve target which is High score rate and 10,000 participants. The CPD activities only achieve Middle score rate and only 5,437 participants involved. In 2021, getting High score rate and 10,000 participants are the goal to achieve. 

## Dataset Description
For this project, I'm using the CPD Analysis Dataset. Continuing Professional Development (CPD) is a combination of approaches, ideas and techniques that will help you manage your own learning and growth. The focus of CPD is firmly on results – the benefits that professional development can bring you in the real world. This dataset contains analysis of CPD used in computing rating and participation prediction in UPM. Prediction of the score rating are based on the classification of activities held and the topic of the activities. This dataset contains 1318 instances and 7 columns. The raw dataset was in `.xlsx` format  

## Hypothesis from Dataset
Based on the dataset that I get, there are several questions that I can come out with:
* Which classification has the lowest score penilaian?
* What is the relationship between rating and participants?
* Does Klasifikasi of activities affect the Score rating? 
* What is the total participants of every classifications?

## Stakeholders
The stakeholders involved in CPD analysis are staff (participants) and also the management. The importances of this project to stakeholders are:
* The management easy to predict the preferences of participants for the next event.
* The management can collect data and analyze the most preferred activities to improve the rating and gain more participant.
* The management can improvise facilities in the universities.
* Participants can easily choose what topic of activity that suitable for them to join.

## Exploratory data analysis steps and examples
Exploratory Data Analysis or EDA is the first and foremost of all tasks that a dataset goes through. EDA lets us understand the data and thus helping us to prepare it for the upcoming tasks.

### Import dataset
`import pandas as pd`

`from google.colab import files uploaded = files.upload()`

`df = pd.read_excel(io.BytesIO(uploaded['CPD for rpm and colab.xlsx']))`

### Identifying the summary of a DataFrame
This method prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.

![2021-02-07 (2)](https://user-images.githubusercontent.com/77633676/107124112-cad54380-68dc-11eb-9c1e-b709c23a06c5.png)

### Visualizations using PowerBI
![2021-02-07 (3)](https://user-images.githubusercontent.com/77633676/107124304-163c2180-68de-11eb-93af-cb8fd9bdd948.png)

### Answers of Questions based on Visualizations
* Which classification has the lowest score penilaian? - KAP has the lowest score rating.
* What is the relationship between rating and participants? - Higher participants, higher score given. 
* Does Klasifikasi of activities affect the Score rating? - Yes. Every Klasifikasi of activities have different score rating.
* What is the total participants of every classifications? - CPD-287, KAP-94, OLCPD-3666, PBP-937, PicTL-453

## Data Preprocessing
Data preprocessing is a data mining technique that involves transforming raw data into an understandable format. Real-world data is often incomplete, inconsistent, and/or lacking in certain behaviors or trends, and is likely to contain many errors. To resolve such issues, data preprocessing must be done.

### Data Cleaning
In data cleaning stage, unwanted data or noises from the dataset will be removed. The goal is to clean the data in such a way that all data can be successfully converted into a numerical type.
These are the steps of data cleaning:-
1)	Select each attributes in the excel file that need to be cleaned. 
2)	Click on Data at the above section and enter filter.
3)	Select the small box at the attributes and it will shows the list of data for each attributes.
4)	Tick the blanks data then click remove data to delete unwanted data in the specific attributes.
5)	Continue the process for the next attributes until the last attributes in the Excel file to ensure the next process is smooth and valid.
6)  Remove unimportant attributes 

### VLOOKUP
There are some purpose that lead us to do the VLOOKUP formula. It is because we need to sort the ‘Latihan’ in the Sheet 2 into each ‘Purata Skor Penilaian Keseluruhan’ in the Sheet 1 that I already renamed as ‘CSkor’. It will automatically construct each of the ‘Tajuk Latihan’ with specific score that given and counted in average. Here the steps that I used to do the VLOOKUP:
1)	Create an attribute which I named as Skor Penilaian in the dataset that need to have new information.
2)	Then state the VLOOKUP formula at the Formula Bar above the attributes of the dataset.

![2021-02-07 (9)](https://user-images.githubusercontent.com/77633676/107127104-da5d8800-68ee-11eb-9654-e02cca828d55.png)

Besides,  I also came out with an initiative to create an another attributes to classify the score of the events into three classes which are Low, Middle and High. The atrribute's name is ‘Skor Klasifikasi’. The attributes will help us in the Model Performances later on.

![2021-02-07 (11)](https://user-images.githubusercontent.com/77633676/107127220-95862100-68ef-11eb-9e7e-c2bd0f763582.png)


### Change Data type
By performing EDA, I found out that the majority of the features in the data set are objects. So, I need to change it into numerical values.
These are the example on how I change the data type from object into int:

`df = df.replace({"Klasifikasi":  {"PBP":1,"KAP":2, "CPD":3}})`

`df = df.replace({"Skor Klasifikasi":  {"High":1,"Middle":2, "Low":3}})`

All data type have been changed into numerical values.

![ssdm](https://user-images.githubusercontent.com/77633676/107126550-8ef5aa80-68eb-11eb-945e-4e995ca1b288.jpeg)

### Splitting dataset into training and test set
I need to split data-set into two separate sets whic is training set and test set for machine learning model. Well here it’s your algorithm model that is going to learn from your data to make predictions. Generally we split the data-set into 70:30 ratio or any other test size. 70 percent data will be taken into train and 30 percent data will be taken into test. However, this splitting can be varies according to the data-set shape and size.

![2021-02-07 (7)](https://user-images.githubusercontent.com/77633676/107126847-3de6b600-68ed-11eb-8e36-24d5553baf21.png)

## Descriptive and Predictive Data Mining
### Descriptive Data Mining
### Predictive Data Mining

## Data Mining Performances Comparison

## Conclusion
* All the model show increase in accuracy after tuning
* The best model goes to **Decision Tree** in predictive data mining with the accuracy of 100% 
* Accuracy 100% was obtained because the dataset is overfit and easy to predict 

## Reflection
* Learn to visualize the hypothesis into interactive visualization
* Experienced in using software tool : PowerBI, Tableau, RapidMiner, and Google Colaboratory-Python 
* Learn that Exploratory Data Analysis is a vital step in a data science project. The main pillars of EDA are data cleaning, data preparation, data exploration, and data visualization. 
* Learn the scope of work of data scientist
* Such an incredible journey throughout the one semester learning Data Mining with Dr Fadhlina in doing all the tasks and projects.
Thank you to my Data Mining lecturer, Dr Fadhlina for all the knowledges and efforts in teaching this course!

