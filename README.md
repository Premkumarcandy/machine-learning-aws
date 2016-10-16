# Workshop: Machine Learning in AWS 

**Requirement for the data set**

The data set has to be a csv-file where each row is an observation.  

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








