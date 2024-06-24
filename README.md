# Exploratory Data Analysis: Online shopping in retail
## Description
This Exploratory Data Analysis (EDA) project was part of AiCore's training for their Data Analysis course. The purpose is to provide real-world experience of data analysis by exploring a dataset of online shopping website activity. 
![Alt text](https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/monthly_revenue.png)
## Table of Contents
1. [Description](#description)
1. [Introduction](#introduction)
1. [What I learnt from the project](#what-i-learnt-from-the-project)
1. [File structure](#file-structure)

## Introduction
The project will showcase the power of EDA in uncovering valuable insights from large datasets and how these insights can be leveraged to drive business success. 

The data contains information about the website activity of users over a one year period. Each sample represents the user interacting with the website during a shopping session. 

A variety of statistical and visualisation techniques will be used to explore the data. The analysis will provide a better understanding of customer behaviour but also help the business optimise marketing strategies and improve their customer experience.

The project is split across 4 key milestones:
1. Setting up the environment. 
1. Extracting the online shopping data from the cloud.
1. Exploratory Data Analysis (EDA).
1. Analysis and Visualisation.

## What I learnt from the project:
Below are examples of how this project has supported my learning:
1. Milestone 1:
    - How to set up a dev environment. Although I set up a directory to store my data and files, initially I did not set up a conda environment. 
        - This was established later, and is a crucial way to set up the specific packages for that particular project. Helpful to not only keep the environment separate from the base, but also enables easier sharing and collaboration. 
    - How to set up and use git and GitHub repo for version control. 
1. Milestone 2:
    - The PyYAML package safe_load function can be used to securely load security credentials, returning them as a dictionary. 
    - The unpacking operator (**) can be used to unpack a dictionary into keyword arguments of a function. This was useful for creating the database URL.
    - How to use the sqlalchemy create_engine function to create a Dialect object tailored towards PostgreSQL, as well as a Pool object which establishes a DBAPI connection.
1. Milestone 3:
    - I used a Jupyter Notebook to document the EDA process. This notebook enables the use of code and markdown cells. Crucially this provides a single space to test code as well as write desriptive notes to document the aim, observations and discuss next steps. 
    - Two separate .py files were created to keep code for transformations and graphical analysis separate. These modules could then be imported into the Jupyter Notebook. Grouping code into similar functions helps make the code more readable. 
        - Crucially, I can see that the classes I have created being used in future EDA projects.
        - I have tried to think about how best to write my code in order for it to be useful in the future. For e.g. in the transformations module I have frequently used *args as the attribute instead of the one column required in the task. This will allow me to make transformations to many columns.
    - I discovered that astype data type conversion to int64 may not work if the data contained nulls. Considering that I had not dealt with the nulls I wanted to change the data type anyway. I found that the Dtype could be converted to Int64 instead.
    - I had initially changed the "_duration" columns to timedelta64 which I thought was more appropriate than float. However, this format proved to be harder to visualise and compare as numerical data. Therefore, I stuck with float.
    - The missingno package contains useful functions to visualise the null values in a dataset. Particularly to identify the amount and spread of the null-values. 
    - Transforming the data (including removing null values and correcting skew) has a degree of subjectivity to the method. But this can be supported by visualising the data and use of statistical methods. E.g. the use of the Chi^2 test to analyse trends in frequency of null-values in correlated variables. 
    - Correcting the skew of datasets with high zero-value counts can be helped by first transfroming the data by adding one. Removing zero enables the use of the Box-Cox method and improves the log transform method.
    - Using boxplots, histograms and scatter plots can be useful visual methods to identify outliers. However, care must be used when doing-so because e.g. high zero-value count data could falsely create outliers. 
    - Outliers in non-numeric data can be harder to spot. But by scrutinising the data, the chance of outliers can be minimised. E.g. grouping low count values into a "Other" category. 
    - Overly correlated variables can cause issues when modelling the data. Overly correlated variables can be identified using a heatmap plot. But should be analysed using statistical methods, e.g using a linear regression model. 
1. Milestone 4:
    - Useful at this stage to save a copy of the cleaned dataset.
    - Gained experience using Pandas, matplotlib, plotly and seaborn to build visualisations. 
    - Using a new variable to create a copy of the df allows it to be manipulated without affecting the original df. This is useful if the new df will be referenced several times. E.g. df of data where a sale was made.
    - Creating functions can be useful to analyse numerical data. E.g. comparing time spent on different tasks.
    - Often plots can be adapted to change titles, legends, sizes, colours etc.
    - Analysis is as much about understanding what questions can be answered (thinking about the limitations of the data) as it is having the skills to perform the analysis.
    - Groupby function provides a powerful method for grouping and analysing data.
    - It is important to consider how the data was cleaned and transformed before conclusions can be made on analysis. E.g. using log transform can lead to negative values. Care must be made when determining max and min values.
    - It is useful to analyse total counts as well as probability/percentages from normalised data.
## Installation
git clone https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917.git

Note: Database access limited to those with login credentials.
## File structure

## Usage

## Licence
None
