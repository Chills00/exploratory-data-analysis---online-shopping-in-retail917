# Exploratory Data Analysis: Online shopping in retail
<p align="center">
    <img src="https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/analytics_gif.gif" width="400" height="400" />
</p>

## Description
This Exploratory Data Analysis (EDA) project was part of AiCore's training for their Data Analysis course. The purpose is to provide real-world experience of data analysis by exploring a dataset of online shopping website activity. This project will provide me with experience using python to extract, load and transform large datasets before performing data analysis to generate meaningful visuals. For example:

<p align="center">
    <img src="https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/monthly_revenue.png" width="400" height="400" />
</p>

![section_break](https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/rainbow.png)

## Table of Contents
1. [Description](#description)
1. [Introduction](#introduction)
1. [Installation](#installation)
1. [File structure](#file-structure)
1. [Usage](#usage)
1. [Licence](#licence)

![section_break](https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/rainbow.png)

## Introduction
The project will showcase the power of EDA in uncovering valuable insights from large datasets and how these insights can be leveraged to drive business success. 

### The Dataset
The data contains information about the website activity of users over a one year period. Each sample represents the user interacting with the website during a shopping session. In total, the dataset represents over 200,000 customer interactions with the website. 

### Analysis
A variety of statistical and visualisation techniques was used to explore the data. The analysis results in a better understanding of customer behaviour which provides oportunity to optimise the companies marketing strategies and improve the customer experience.

The project is split across 4 key milestones:
1. Setting up the environment. 
1. Extracting the online shopping data from the cloud.
1. Exploratory Data Analysis (EDA).
1. Analysis and Visualisation.

![section_break](https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/rainbow.png)

## Installation
1. Clone repo:
    ```
    git clone https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917.git
    ```  

1. Using a CLI install conda environment on your local machine:
    ```
    conda env create -f environment.yaml 
    ```  


Note: Database access limited to those with login credentials.

![section_break](https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/rainbow.png)

## File structure

AiCoreEDA_Project  
├── db_utils.py  
├── df.info.py  
├── transformations.py  
├── plotter.py  
├── EDA_notebook.ipynb  
├── Analysis_Notebook.ipynb  
└── README.md  

![section_break](https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/rainbow.png)

## Usage
### Python files:
- db_utils.py:
    - Uses Sqlalchemy to connect to remote database and creates .csv file of downloaded data.
- db_info.py:
    - Class used to generate basic info about a dataframe, including data types, descriptive statistics, df shape and null values. 
- transformations.py:
    - Contains two classes, one to perform transformations on the data and the second to perform transformations on the dataframe.
    - Data transformations include changing the data type.
    - Dataframe transformations include reoval of null-values (drop columns/rows), imputing data with mean/median/mode, and performing transformations to correct skewed data.
- plotter.py:
    - Contains a class used to generate plots to visualize a dataset for statistical analysis.
    - Visualisations include, visualisation of null-values, bar chart, histogram, heatmaps, boxplots, etc.
    - Also contains statistical tests including the chi squared test, and k squared test.
    - Additionally, there are methods to generate visuals to assess normalisation of data to correct for skew. 

### Jupyter Notebooks:
- EDA_notebook.ipynb:
    - Contains the workflow of the initial EDA process including data extraction, loading and cleaning/transformations. 
    - Key steps included:
        - Correcting data types.
        - Handling missing values.
        - Obtaining basic info on df.
        - Checking and correcting distribution.
        - Handling outliers.
        - Checking for overly correlated data. 
- Analysis_Notebook.ipynb:
    - Contains the workflow for a more detailed analysis and visualisation of the data.
    - Key questions addressed:
        - Where are our customers spending their time?
        - What software are our customers using?
        - What factors are influencing revenue?

![section_break](https://github.com/Chills00/exploratory-data-analysis---online-shopping-in-retail917/blob/main/rainbow.png)

## Licence
None
