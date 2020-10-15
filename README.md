# Machine Learning Engineer Nanodegree Capstone Project
## Customer Segmentation Report for Arvato Financial Services


### Table of Contents

1. [Requirements](#requirements)
2. [Project Overview](#overview)
3. [Dataset](#dataset)
4. [Results](#results)
5. [Licensing and Acknowledgements](#licensing)


## Requirements <a name="requirements"></a>
All of the requirements are provided in requirements.txt. Use: pip install -r requirements.txt

## Project Overview<a name="overview"></a>
“A Customer Segmentation Report for Arvato Financial Solutions” was one of the proposed projects for the Machine Learning Engineer Nanodegree Program by the Udacity. The main objective of the project is to determine the descriptive portrait of the potential customer and are chances that a new person from the targeted mailout campaign could become a new customer.
Arvato has provided several dataset files that have demographic information about the general population of Germany, current customers of the company, targeted mailout campaign outcomes, and two files with a description of the demographic features.

The project is divided into several subtasks:
1.	Data Analysis and Preprocessing;
2.	Customer Segmentation Report;
3.	Supervised Learning Predictive Model;
4.	Kaggle Competition;

The training data is protected under the Terms and Conditions and is unavailable for public sharing.


## Dataset <a name="dataset"></a>
All the data is provided by Bertelsmann Arvato Analytics and there are given four files for this project:
* `Udacity_AZDIAS_052018.csv`: Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns).
* `Udacity_CUSTOMERS_052018.csv`: Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns).
* `Udacity_MAILOUT_052018_TRAIN.csv`: Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns).
* `Udacity_MAILOUT_052018_TEST.csv`: Demographics data for individuals who were targets of a marketing campaign; 42 833 persons (rows) x 366 (columns).
Additionally, there were 2 more files for describing attributes:
* `DIAS Attributes - Values 2017.xlsx`: Explains values encoding 
* `DIAS Information Levels - Attributes 2017.xlsx`: Explains column names meanings

Each row in the demographic data files represents and describes a person as well as his or her environment, such as their household, building, and neighborhood. The general structure of the AZDIAS and CUSTOMERS data files is similar. MAILOUT...TEST and MAILOUT…TRAIN are provided for the development and testing of the supervised model.
The training data is protected under the Terms and Conditions and is unavailable for public sharing.


## Instructions <a name="instructions"></a>
The dataset used in this project is proprietary. As so this project is not usable for those outside of this nanodegree, it does serve as a snapshot of the strategies I chose to use to approach this challenge.


## Results <a name="results"></a>
According to the 2nd part of the project with customers segmentation, the fact of a person being a potential customer is positively affected by the actuality of the last transaction, gender, whether the person from GDR or FRG, with fine social status, the person is dominant minded and dreamily, and fine family type. While financial typology: money saver, number of 6-10 family houses in the PLZ8, and density of inhabitants per square kilometer have a negative impact.

According to the 3rd part of the project with supervised models, the final predictions were made on the Udacity_MAILOUT_052018_TEST.csv, which was pre-processed as the training set. While the private score of the final performance of my model was 0.79, on Kaggle competition it managed to hold 0.79 of accuracy as well according to the AUC-ROC evaluation metric. 


## Licensing and Acknowledgements<a name="licensing"></a>
Data belongs to the Bertelsmann Arvato Analytics, Udacity and Kaggle. The solutions are free for use. 
