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
* Experiment Setting: Hyperparameter Tuning
* Result and Analysis
* Data Product
* Conclusion
* Reflection

## Problem Statement
From the CPD analysis, I found out the rating score given by the participants and number of participants in 2020 does not achieve target which is High score rate and 10,000 participants. The CPD activities only achieve Middle score rate and only 5,437 participants involved. In 2021, getting High score rate and 10,000 participants are the goal to achieve. 

## Dataset Description
For this project, I'm using the CPD Analysis Dataset. Continuing Professional Development (CPD) is a combination of approaches, ideas and techniques that will help you manage your own learning and growth. The focus of CPD is firmly on results – the benefits that professional development can bring you in the real world. This dataset contains analysis of CPD used in computing rating and participation prediction in UPM. Prediction of the score rating are based on the classification of activities held and the topic of the activities. This dataset contains 1318 instances and 7 columns.  The raw dataset was in `.xlsx` format  

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

Observation:
1. From the first diagram, we can see that the 'Skor Penilaian' is decreasing where Fakulti Perubatan & Sains Kesihatan has the highest 'Skor Penilaian' (803.64) and the lowest 'Skor Penilaian' is Fakulti Pengajian Alam Sekitar (4.62).
2. We can see that the KAP has the highest average of 'Jumlah Jam' which is 37.12 hours and KAP also has the highest average of 'Skor Penilaian' which is 4.79 compared to CPD and PBP.
3. PBP has the highest 'Skor Penilaian' by Klasifikasi which is 4481.95 while KAP has the lowest 'Skor Penilaian' which is 450.17.
4. The highest 'Jumlah Jam' by 'Tajuk Latihan and 'Tempat Latihan' is 81 hours (24.18%) where the 'Tajuk Latihan' is KURSUS SISTEM PUTRABLAST V3.8(SIRI-9 FSPM UPMKB) and the 'Tempat Latihan' is MAKMAL D ICT, UPMKB.
5. 'Skor Penilaian' of Klasifikasi (PBP) and Tajuk Latihan (MAJLIS PERASMIAN & ASPIRASI NC SEMPENA BULAN PENDIDIK UPM 2020) is 785.40 which is the highest score.

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

### Data Integration
Data integration is the merging of data from various sheets into one new sheets. Data integration is performed on the attribute which identifies unique entities. It needs to be done carefully because errors in data integration can produce deviant results and even misleading the action later. 

### Data Selection
The data that from the dataset given is often not all used, therefore I took the initiative to remove unimportant attributes.

### VLOOKUP
There are some purpose that lead us to do the VLOOKUP formula. It is because we need to sort the ‘Latihan’ in the Sheet 2 into each ‘Purata Skor Penilaian Keseluruhan’ in the Sheet 1 that I already renamed as ‘CSkor’. It will automatically construct each of the ‘Tajuk Latihan’ with specific score that given and counted in average. Here the steps that I used to do the VLOOKUP:
1)	Create an attribute which I named as Skor Penilaian in the dataset that need to have new information.
2)	Then state the VLOOKUP formula at the Formula Bar above the attributes of the dataset.

![2021-02-07 (9)](https://user-images.githubusercontent.com/77633676/107127104-da5d8800-68ee-11eb-9654-e02cca828d55.png)

Besides,  I also came out with an initiative to create an another attributes to classify the score of the events into three classes which are Low, Middle and High. The atrribute's name is ‘Skor Klasifikasi’. The attributes will help us in the Model Performances later on.

![2021-02-07 (11)](https://user-images.githubusercontent.com/77633676/107127220-95862100-68ef-11eb-9e7e-c2bd0f763582.png)


### Data Transformation
Data is converted or combined into a format suitable for processing in data mining. Some data mining methods require special data formats before they can be applied.
By performing EDA, I found out that the majority of the features in the data set are objects. So, I need to change the data type into numerical values.
These are the example on how I change the data type from object into int:

`df = df.replace({"Klasifikasi":  {"PBP":1,"KAP":2, "CPD":3}})`

`df = df.replace({"Skor Klasifikasi":  {"High":1,"Middle":2, "Low":3}})`

All data type have been changed into numerical values.

![ssdm](https://user-images.githubusercontent.com/77633676/107126550-8ef5aa80-68eb-11eb-945e-4e995ca1b288.jpeg)

### Splitting dataset into training and test set
I need to split data-set into two separate sets which is training set and test set for machine learning model. Well here it’s your algorithm model that is going to learn from your data to make predictions. Generally we split the data-set into 70:30 ratio or any other test size. 70 percent data will be taken into train and 30 percent data will be taken into test. However, this splitting can be varies according to the data-set shape and size.

![2021-02-07 (7)](https://user-images.githubusercontent.com/77633676/107126847-3de6b600-68ed-11eb-8e36-24d5553baf21.png)

## Descriptive and Predictive Data Mining
### Descriptive Data Mining
Descriptive data mining is under unsupervised learning. A descriptive model describes a system or other entity and its relationship to its environment. It is generally used to help specify and/or understand what the system is, what it does, and how it does it. The methods come under this type of mining category are called association, clustering, and summarization. For this case, I chose Clustering as the method for the process and K-Mean is the model of the machine learning algorithm.
These are steps in developing descriptive data mining solution in Python:
1. Choose the right number of cluster(k) by performing elbow method
2. k-value is obtained by picking the fewest number of clusters that reduces the average distance. After k-value, the graph is almost linear.
3. Once k-value is obtained, we can visualize the clustering using matplotlib.

For RapidMiner:
![kmeans](https://user-images.githubusercontent.com/77633676/107358607-8e892980-6b0e-11eb-9a47-1a2cc79ab6d0.png)

For k-means:
* Read - Read in RapidMiner is used to read the data folder that have been input into the process.
* Select Attribute - Select attributes mainly used for separating the used and unused attributes in order to calculate the attribute. For this case, I select 'Klasifikasi' attribute to count each participant.
* Clustering - Select the model of the Clustering which is K-Means.
* Cluster Model Visualization - This cluster model visualization is used to visualize the model of the clustering which is k-Means.


### Predictive Data Mining
Predictive analytics is the process by which information is extracted from existing datasets for determining patterns and predicting the forthcoming trends or outcomes.
The methods come under this type of mining category are called classification, time-series analysis, and regression. For this case, I chose Classification as the method for the process.
These are the steps in developing descriptive data mining solution in Python:-
1. Import required libraries
2. Import and upload file into GoogleColab
3. Load data and read file that has been imported
4. Divide given columns into two types of variables dependent (or target variable) and independent variable (or feature variables)
5. Import required classifier
6. Print the accuracy of the model (Decision Tree and Random Forest)

For RapidMiner:
![dtree](https://user-images.githubusercontent.com/77633676/107356545-e8d4bb00-6b0b-11eb-801f-f53e16b4ff20.png)
![rforest](https://user-images.githubusercontent.com/77633676/107356765-29cccf80-6b0c-11eb-98d0-ec7a63ddc7e5.png)

In RapidMiner,  I implemented a new thing which is Discretize.  I will explain the function of each parameters that I used in the RapidMiner in order to process my decision making:
* Retrieved - Retrieved in RapidMiner is used to input the data folder into the process. We can also use Read parameter but it is slower since it needs to process each time when you fill in the data. However, by using retrieved, you just need to do it once since you already saved the file in the repository in the application.
* Discretize by Frequency - Discretized by Frequency is used when you want the sort or separate the implement into each of class that you already classified in the Excel and edit the number of bins based on class you have stated. 
* Nominal to Binominal -  Nominal to Binominal operator is used for changing the type of nominal attributes to a binominal type. This operator not only changes the type of selected attributes but it also maps all values of these attributes to binominal values i.e. true and false.
* Set Role- I'm using set role to determine the special attributes that we need to count. 
* Select Attributes - Select attributes mainly used for separating the used and unused attributes in order to calculate the attribute.
* Split Data - In split data, it will be boxes that we can fill to put ratio of our studies over 1.0. The top box usually 0.7 and below will be 0.3. But in some cases, people also put 0.8 and 0.2. The higher of top box the lower accuracy you can get formulally. 
* Decision Tree / Random Forest - Decision tree and Random Forest are common models that people use to predict things in RapidMiner. Normally, they are used to calculate the classification, the characterized data not numerical.
* Apply Model - In apply model, it is for applying the parameters that we stated behind it. It also have goal to predict the unseen data and to transform data into a preprocessing model.
* Performance - It will make the models compatible and do generating the result.

## Experiment Setting: Hyperparameter Tuning
The process of finding most optimal hyperparameters in machine learning is called hyperparameter optimisation. There are 3 commons algorithms which are Grid Search, Random Search, and Bayesian Optimisation. In this case, I decided to use Grid Search for hyperparameter tuning. 
Grid search is arguably the most basic hyperparameter tuning method. With this technique, we simply build a model for each possible combination of all of the hyperparameter values provided, evaluating each model, and selecting the architecture which produces the best results. For example, we would define a list of values to try for both n_estimators and max_depth and a grid search would build a model for each possible combination. The diagram below shows the suggested values after hyperparameter tuning has been done for decision tree model:

![2021-02-08 (11)](https://user-images.githubusercontent.com/77633676/107240782-43670c00-6a65-11eb-9540-7dff67580691.png)

After the suggested values have been used to obtain new accuracy, we can see that the hyperparameter tuning makes the accuracy increase from 89.27% to 97.18%. Thus, the performance is increasing as well.

## Result and Analysis
### Data Mining Performances Comparison (RapidMiner)
#### Decision Tree
For High 'Skor Klasifikasi'
![2021-02-09 (20)](https://user-images.githubusercontent.com/77633676/107385549-f3a04780-6b2d-11eb-9842-1ee540e4c65e.png)
![2021-02-09 (22)](https://user-images.githubusercontent.com/77633676/107385644-0adf3500-6b2e-11eb-84e5-f5db6103d7c0.png)
For Middle 'Skor Klasifikasi'
![2021-02-09 (24)](https://user-images.githubusercontent.com/77633676/107386034-6dd0cc00-6b2e-11eb-877d-3ed9cd99c778.png)
![2021-02-09 (26)](https://user-images.githubusercontent.com/77633676/107386145-893bd700-6b2e-11eb-8464-b7f633551a42.png)
For Low "skor Klasifikasi
![2021-02-09 (29)](https://user-images.githubusercontent.com/77633676/107386542-e8015080-6b2e-11eb-874c-b536be113d3d.png)
![2021-02-09 (30)](https://user-images.githubusercontent.com/77633676/107386617-fbacb700-6b2e-11eb-9530-f6ad32afa69b.png)
Auto Model
![2021-02-09 (34)](https://user-images.githubusercontent.com/77633676/107387707-0d428e80-6b30-11eb-989d-8129b0047c3b.png)
![2021-02-09 (35)](https://user-images.githubusercontent.com/77633676/107387769-1cc1d780-6b30-11eb-9241-e1d5fa196c9e.png)

#### Random Forest
![2021-02-09 (38)](https://user-images.githubusercontent.com/77633676/107388040-601c4600-6b30-11eb-8f19-cf5e5b1921b1.png)
![2021-02-09 (40)](https://user-images.githubusercontent.com/77633676/107388295-a7a2d200-6b30-11eb-9884-62d36b0554fe.png)


### Data Mining Performances Comparison (Tuning)
Ratio 50:50
![2021-02-09 (12)](https://user-images.githubusercontent.com/77633676/107375012-3c063800-6b23-11eb-8dc0-df1a9a2aba81.png)
Ratio 70:30
![2021-02-09 (14)](https://user-images.githubusercontent.com/77633676/107375151-648e3200-6b23-11eb-99d5-28c9b6b39751.png)
Python- Ratio 50:50, 70:30
![2021-02-09 (18)](https://user-images.githubusercontent.com/77633676/107382838-4e846f80-6b2b-11eb-9a32-d8357ce3ee8a.png)

In conclusion, all the model show increase in accuracy after hyperparameter tuning. The best model goes to **Decision Tree** in predictive data mining with the accuracy of 97.18% after hyperparameter tuning. Accuracy obtained is near 100% because the dataset is overfit and easy to predict.

## Data Product
![2021-02-09 (9)](https://user-images.githubusercontent.com/77633676/107395993-4ed73780-6b38-11eb-991e-4815d4a5cbe7.png)
* Build web app by using Streamlit
* The function of this web app is to predict the score rating by participant based on the attributes in the dataset which are Klasifikasi, Tajuk Latihan, Tempat Latihan, Jabatan, and Jumlah Jam.
* Stakeholders : Staff & Management 

## Conclusion
From this project, I managed to provide results based on the classification of score which are High, Middle, and Low from the participants' feedbacks. The stakeholders which is the management can measure the performance of their events and can make improvement for next events.

![2021-02-10 (2)](https://user-images.githubusercontent.com/77633676/107395382-b6d94e00-6b37-11eb-916d-466e164340c3.png)
![2021-02-10 (3)](https://user-images.githubusercontent.com/77633676/107395449-c8baf100-6b37-11eb-8df8-3f5e5dca1401.png)
![2021-02-10 (5)](https://user-images.githubusercontent.com/77633676/107395508-da03fd80-6b37-11eb-8db7-76c9e0a95098.png)


## Reflection
From this project, I've learnt to visualize the hypothesis into interactive visualization. Also, I gain experience in using software tool such as PowerBI, Tableau, RapidMiner, and Google Colaboratory:Python. This project also makes me realize that Exploratory Data Analysis is a vital step in a data science project. The main pillars of EDA are data cleaning, data preparation, data exploration, and data visualization. The most interesting part is I've learn the scope of work of data scientist which is very exciting. It is such an incredible journey throughout this one semester learning Data Mining with Dr Fadhlina in doing all the tasks and projects.
Thank you to my Data Mining lecturer, Dr Fadhlina for all the knowledges and efforts in teaching this course!

