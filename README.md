# Workshop: Machine Learning in AWS 

**Requirement for the data set**

The data set has to be a csv-file where each row is an observation. The data set cannot be missing more than 10000 values. 

We have chosen a dataset from the archive of UC Irvine (http://archive.ics.uci.edu/ml/). The set contains variables for predicting whether a person has an income of more than 50K based on age, education, marital-status etc*. 

The data set consits of two parts: 
- *training-data.csv*: A file containing 32561 rows of labeled data. Each row contains all the variables for the observation and a label describing whether the observation has an income above 50K (1) or not (0). 

- *unpredicted.csv*: A file containing 16281 rows of unlabeled data. All observations in this file get predicted by our model. 

*Comlete list of variables: age, workclass, final-weight, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country

## Upload the data sets to Amazon

Amazon Machine Learning can load data from either Amazon S3 og Amazon Redshift. We have chosen to use Amazon S3. 

1. Create a new S3 Bucket 
2. Upload the two .csv-files from this github-repo to the bucket


## Create a datasource of the data sets 

First we want to create a datasource. A datasource is an Amazon Machine Learning object that contains the location of your input data and important metadata about your input data. 

1. Choose Machine Learning under Analytics
2. Choose a region (must be North Virginia or Ireland at this point)
3. Click on “Get started”
4. Click on “View Dashboard”
5. Click on “Create a new datasource”

### Input data
We are going to use training-data.csv to create and train a machine learning model. 

1. Type in the name of the bucket you just created. Choose the file called training-data.csv. You are not required to give the datasource a name.
2. Grant permission for Amazon
3. Click "Continue"

### Schema
1. Answer "Yes" to the question: *Does the first line in your CSV contain the column names?*. Observe that the Name-column now uses the specific variable names instead of the genereic “Var01”, “Var02”...
2. Verify that the column income-over-50K is of the type BINARY.
3. Click "Continue"


### Target
We want to tell Amazon Machine Learning which column we are trying to predict. 

1. Answer "Yes" to the question: *Do you plan to use this dataset to create or evaluate an ML model?*
2. Choose *income-over-50K* as target 
3. Click "Continue"

### Row ID
The Row Id is used if we want to connect each row of the input data to a unique identifier. Our input data does not contain identifier, so choose "No".

### Review
If all looks correct, click **Create Datasource**. This might take some minutes. 

The datasource is ready for use when the datasource's status is *Completed*. The data is so far just uploaded and converted to an Amazon Machine Learning Object. Notice the number for *Records that failed to process*. More than 10000 makes Amazon stop the uploading. 

Amazon offers visualisations of the input data. You can browse the attribues in the menu on the left side. Choose *Categorical*, and look at the preview of the data. This provides data of the attributes in the input data. The graph shows different values of the variable and number of values found. This is an easy way to see whether your data seems correct or not. 


## Create an AWS ML Model 

We want to create a ML Model based on the training set we used in the previous step. This model finds the weights for all the variables, to optimize the prediction. 

On the AWS Machine Learning Dashboard choose **Create new ML Model**

### Input data
1. Choose the option *I already created a datasource pointing to my S3 data*. 
2. Choose the datasource we created based on *training-data.csv*. 
3. Click “Continue”

### ML Model Settings
1. Check that the model is based on *income-over-50K* and that the model type is BINARY.

2. Select a name for the model name and a name for the evaluation. 

We choose to use the default settings. This will split our data set into 2 new sets. 70% of the data will be used to train the model and 30% will be used to test the model afterwards. 

3. Click “Review” and then **Create ML Model**. 

Wait for the model to finish. This might take some time in the meanting, take a look at the ML Dashboard. 

### ML Dashboard

Look at the ML Dashboard. We should have 5 files: 
* The original datasource based on our input file
* Training data set (70% of the original datasource)
* Validation data set (30% of the original datasource)
* A ML Model: The model we just created based on our training set. 
* Evaluation ML Model: The evaluation of our model. 


### Explore performance
1. Choose Evaluation ML Model to see how well the model performed. 

AUC determines how well the model performed where 1 is best and 0 is worst. AUC stands for Area Under the Curv and measures the ability of the model to predict a higher score for positive examples as compared to negative examples.

2. Choose **Explore performance**

This is a visualization of what threshould chosen for our categorization. By adjusting the slider we can see that the percentage of correct will change. This can be used to optimize our model depending on the prerequisitires of the problem. The model can also be adjusted based on accuracy, precision, recall or false positive rate. 

3. Check "Alerts" (left menu) and that there are no alerts. Alerts might be shown if the training data and test data is very different. 



## Predict income 

We are using our model to predict income for data in our unpredicted file. This will be based on the threshould in 

Go to Amazon Machine Learning Dashboard
Choose ML Model 
Generate Batch Predicitons 



### Data for Batch Predictions

For Locate Input Data, choose *My data is in S3, and I need to create a datasource*
Give a name for the unpredicted data
Write the path to the unpredicted file located in S3. 
Choose “Yes” for *Does the first line in your CSV contain the column names?*
Click “Verify” and “Continue”. 

### Batch Prediction Reults

1. Grant permission for Amazon
2. For the S3 desitination for the result; choose the bucket created for this project. 
3. Click “Review” and “Create Batch Prediction”. 

##Evaluation of the Prediction

Go to the bucket we created in S3. 
Under *batch-prediction* look at the following files: 
xxxxxx-manifest
 result/xxxxx-unpredicted.cvs.gz

Download the results from *result/xxxxx-unpredicted.cvs.gz*. This file contains two columns *bestAnswer* and *PredictionScore*. You can compare your prediction results with the actual results (true-results.csv). 

Run the python scripts that compare the predictions with the acutal results: 

`python compare-results.py prediction.csv`

