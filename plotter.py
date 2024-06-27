from scipy import stats
from statsmodels.graphics.gofplots import qqplot
import IPython
import matplotlib.pyplot as plt
import matplotlib.style as style
import missingno as msno
import numpy as np
import seaborn as sns
import plotly.express as px
import pandas as pd

class Plotter():
    '''
    This class is used to generate plots to visualize a dataset for statistical analysis.

    ------------------
    Parameters:
    df_name: Pandas df
        A Pandas dataframe

    ------------------
    Attributes:
    
    ------------------
    Methods:
    missing_no_matrix()
        Plots the pattern of missingness (missing values) in the dataset.
    missing_no_bar()
        Plots a bar chart corresponding to the number of non-null values in each column.
    missing_no_heatmap()
        Plots a heatmap to show the correlation of missingness between every two columns (if containing null values). 
    probability_distribution()
        Calculates the value counts, probabilities, generates a descrete probability distribution plot, and returns the mode, mean and median (if able to calculate).
    correlation()
        Plots a heatmap representing the correlation between two variables.
    correlation_matrix()
        Plots a heatmap representing the correlation between all variables within a dataset. 
    k2_test()
        Calculate the k^2 statistical analysis of goodness-of-fit to normal distribtution.
    qq_plot()
        Generates a Q-Q plot, which is a probability plot for comparing two probability distributions.
    histogram()
        Generates a hitogram to plot the distribution of a numeric variables values as a series of bars.
    density_plot()
        Generates a density plot, which is essentially a smoothed histogram. 
    boxplot()
        Generates a box plot, which displys the summary data including distribution, outliers, median, Q1 and Q3.
    cumulative_distribution_function()
        Generates a CDF plot, which is a graphical representation of the cumulative probability distribution of a random variable.
    scatter()
        Plots a scatter plot, which is used to display the relationship between two (usually continuous) numerical variables.
    chi_squared()
        Calculates the chi^2 value to check to see if there is any trend in the frequency of NaNs in column_a, as a function of column_b
    log_transformation()
        Transforms the data, correcting skewness using the Log transform method and generates histogram and Q-Q plot of the transformed data. 
    boxcox()
        Transforms the data, correcting skewness using the Box-Cox method and generates histogram and Q-Q plot of the transformed data. 
    yeojohnson()
        Transforms the data, correcting skewness using the Yeo-Johnson method and generates histogram and Q-Q plot of the transformed data. 
    skew_subplot()
        Generates a figure with a histogram, Q-Q plot and skewness value for the data series passed to it, and for the same data series transformed using the log transform, Box-Cox and Yeo-Johnson methods.
    pair_plot()
        Generates a scatter plot for each pair of variables.
    count_plot()
        Generates a bar chart for each pair of variables.
    '''
    def __init__(self, df_name):
        self.df_name = df_name
    
    def missing_no_matrix(self):
        '''
        This method plots the pattern of missingness (missing values) in the dataset. 
        Complete datasets are represented by grey bars, while missing values are represented by white lines. 

        Parameters:
            df_name (Pandas df): Pandas df
        
        Returns:
            The matrix plot.
        '''
        try:
            return msno.matrix(self.df_name)
        except:
            print('Unable to generate plot')
    
    def missing_no_bar(self):
        '''
        This method plots a bar chart corresponding to the number of non-null values in each column. 
        
        Parameters:
            df_name (Pandas df): Pandas df
        
        Returns:
            The bar chart.
        '''
        try:
            return msno.bar(self.df_name)
        except:
            print('Unable to generate plot')
    
    def missing_no_heatmap(self):
        '''
        This method plots a heatmap to show the correlation of missingness between every two columns (if containing null values). 
        - A value near -1 means if one variable appears then the other variable is very likely to be missing.
        - A value near 0 means there is no dependence between the occurrence of missing values of two variables.
        - A value near 1 means if one variable appears then the other variable is very likely to be present.

        Parameters:
            df_name (Pandas df): Pandas df
        
        Returns:
            The bar chart.
        '''
        try:
            return msno.heatmap(self.df_name)
        except:
            print('Unable to generate plot')
        
    def probability_distribution(self, column_name):
        '''
        This method calculates the probability of a given value and plots the descrete probability distribution.
        
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed
        
        Returns:
            The value counts, probabilities, the descrete probability distribution plot, mode, mean and median (if able to calculate).
        '''
        value_counts = self.df_name[column_name].value_counts()
        print('Value counts:')
        print(value_counts)
        print()
        # Convert to probabilities
        probs = self.df_name[column_name].value_counts(normalize=True)
        print('Probability:')
        print(probs)
        dpd = sns.barplot(y = probs.values, x = probs.index)
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        plt.show()
        print(f'The mode of the distribution is {self.df_name[column_name].mode()[0]}')
        try:
            print(f'The mean of the distribution is {self.df_name[column_name].mean()}')
        except:
            print('The mean cannot be calculated on this data series')    
        try:
            print(f'The median of the distribution is {self.df_name[column_name].median()}')
        except:
            print('The median cannot be calculated on this data series') 

    def correlation(self, column_a, column_b):
        '''
        This method generates a heatmap by plotting the data as a colour-encoded matrix indicating the correlation between two variables.
        
        Parameters:
            df_name (Pandas df): Pandas df
            column_a (str/object): Name of variable to be analysed
            column_b (str/object): Name of variable to be analysed
        
        Returns:
            The heatmap.
        '''
        try:
            return sns.heatmap(self.df_name[[column_a, column_b]].corr(), annot=True, cmap='coolwarm')
        except:
            print('Unable to generate plot')

    def correlation_matrix(self):
        '''
        This method generates a heatmap by plotting the data as a colour-encoded matrix indicating the correlation between all variables in a df.
        
        Parameters:
            df_name (Pandas df): Pandas df
        
        Returns:
            The heatmap.
        '''
        try:
            return sns.heatmap(self.df_name.corr(), annot=True, cmap='coolwarm')
        except:
            print('Unable to generate plot')

    def k2_test(self, column_name):
        '''
        This method (D'Agostino's K^2 test) is a goodness-of-fit measures of departure from normality.
        The tests assume the default situation (aka. the null hypothesis) is that the distribution is not normally distributed.
        A p-value of less than 0.05 provides significant evidence for the null hypothesis being false, and suggests the data are normally distributed.
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The k^2 statistical analysis.
        '''
        data = self.df_name[column_name]
        stat, p = stats.normaltest(data, nan_policy='omit')
        print('Statistics = %.3f, p = %.3f' % (stat, p))

    def qq_plot(self, column_name):
        '''
        This method generates a Q-Q plot (quantile-quantile plot), which is a probability plot for comparing two probability distributions by plotting their quantiles against each other.
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The q-q plot.
        '''
        plot = qqplot(self.df_name[column_name], scale=1, line='q')
        plt.show()
    
    def histogram(self, column_name):
        '''
        This method generates a hitogram to plot the distribution of a numeric variables values as a series of bars. 
        Each bar is grouped into a bin (which may need to be adjusted depending on the dataset).
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The histogram.
        '''
        self.df_name[column_name].hist(bins=25, legend=True)

    def density_plot(self, column_name):
        '''
        This method generates a density plot, which is essentially a smoothed histogram. 
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The density plot.
        '''
        sns.histplot(data = self.df_name, x = column_name, kde=True)
        sns.despine()
    
    def boxplot(self, column_name):
        '''
        This method generates a box plot, which displys the summary data including distribution, outliers, median, Q1 and Q3.
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The box plot.
        '''
        sns.boxplot(y = self.df_name[column_name], color='royalblue', showfliers=True)
     
    def cumulative_distribution_function(self, column_name):
        '''
        This method generates a cumulative distribution function (CDF) plot. 
        This is a graphical representation of the cumulative probability distribution of a random variable. The x-axis covers the range of values the variable takes, while the y-axis represents the cumulative probability from 0 to 1. The plot displays how the probabilities accumulate as the variable increases, providing insights into the overall distribution of the data, including central tendency, spread, and skew. It is particularly useful for comparing multiple distributions or assessing the goodness-of-fit for a given distribution.
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The CDF plot.
        '''
        sns.histplot(self.df_name[column_name], cumulative=True, stat='density', element='poly')
        plt.title('Cumulative Distribution Function (CDF)')
        plt.xlabel(column_name)
        plt.ylabel('Cumulative Probability')
    
    def scatter(self, column_a, column_b):
        '''
        This method generates a scatter plot, which is used to display the relationship between two (usually continuous) numerical variables.
        Each point on the plot represents an observation in the dataset and is placed according to the values of the two variables it represents.
        Scatter plots are particularly useful in identifying trends, patterns, and potential correlations between variables, as well as in spotting outliers. They are often used as a basis for curve fitting and regression, as they show each individual data point, and so make it easy to visualise residuals (the difference between the observed and modelled values).
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_a (str/object): Name of variable to be analysed
            column_b (str/object): Name of variable to be analysed

        Returns:
            The scatter plot.
        '''
        sns.scatterplot(data=self.df_name, x=column_a, y=column_b)

    def chi_squared(self, column_a, column_b):
        '''
        This method calculates the chi^2 value to check to see if there is any trend in the frequency of NaNs in column_a, as a function of column_b.
        The Chi-squared test is a statistical hypothesis test that is used to determine whether there is a significant association between two categorical variables in a sample.
        A p-value greater than 0.05 suggests that the NaNs are randomly distributed with respect to the value of column_b.
  
        Parameters:
            df_name (Pandas df): Pandas df
            column_a (str/object): Name of variable to be analysed
            column_b (str/object): Name of variable to be analysed

        Returns:
            The chi^2 statistical analysis.
        '''
        self.df_name['missing_values'] = self.df_name[column_a].isnull()
        contingency_table = pd.crosstab(self.df_name['missing_values'], self.df_name[column_b])
        chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
        print(f"Chi-square statistic = {chi2}")
        print(f"p-value = {p}")

    def log_transformation(self, column_name):
        '''
        This method transforms the data using the Log transform method and generates histogram and Q-Q plot of the transformed data. 
        The transformation involves replacing each value x with log(x) (except from 0).
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The histogram and Q-Q plot.
        '''
        log = self.df_name[column_name].map(lambda i: np.log(i) if i > 0 else 0)
        t = sns.histplot(log, label = 'Skewness: %.2f' % (log.skew()), kde=True)
        t.legend()
        qq_plot = qqplot(log, scale = 1 ,line = 'q', fit=True)
        plt.show()
    
    def boxcox(self, column_name):
        '''
        This method transforms the data using the Box-Cox method and generates histogram and Q-Q plot of the transformed data. 
        The data must be positive.
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The histogram and Q-Q plot.
        '''
        boxcox = self.df_name[column_name]
        boxcox= stats.boxcox(boxcox)
        boxcox= pd.Series(boxcox[0])
        t=sns.histplot(boxcox,label="Skewness: %.2f"%(boxcox.skew()), kde=True)
        t.legend()
        qq_plot = qqplot(boxcox, scale = 1 ,line = 'q', fit=True)
        plt.show()
    
    def yeojohnson(self, column_name):
        '''
        This method transforms the data using the Yeo-Johnson method and generates histogram and Q-Q plot of the transformed data. 
                        
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The histogram and Q-Q plot.
        '''
        yeojohnson = self.df_name[column_name]
        yeojohnson = stats.yeojohnson(yeojohnson)
        yeojohnson = pd.Series(yeojohnson[0])
        t=sns.histplot(yeojohnson,label="Skewness: %.2f"%(yeojohnson.skew()), kde=True)
        t.legend()
        qq_plot = qqplot(yeojohnson, scale = 1 ,line = 'q', fit=True)
        plt.show()
    
    def skew_subplots(self, column_name):
        '''
        This method is used to compare the transformation methods effect on skew. 
        It generates a figure with a histogram, Q-Q plot and skewness value for the data series passed to it, and for the same data series transformed using the log transform, Box-Cox and Yeo-Johnson methods.
                        
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The a figure with a histogram, Q-Q plot and skewness value for the data series passed to it, and for the same data series transformed using the log transform, Box-Cox and Yeo-Johnson methods.
        '''
        #Create a figure with four subplots
        sns.set()
        fig, axs = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))
        fig.subplots_adjust(hspace=0.4, wspace=0.3)
        fig.suptitle(f'Transformation effect on skewness value for {column_name}')

        # Original data
        sns.histplot(ax=axs[0,0], data=self.df_name[column_name], label = 'Skewness: %.2f' % (self.df_name[column_name].skew()), kde=True)
        axs[0,0].set_title('Original Data Histogram')
        axs[0,0].legend()
        qqplot(ax=axs[1,0], data=self.df_name[column_name], scale = 1 ,line = 'q', fit=True)
        axs[1,0].set_title('Original Data Q-Q Plot')

        # log transform data
        log = self.df_name[column_name].map(lambda i: np.log(i) if i > 0 else 0)
        sns.histplot(ax=axs[0, 1], data=log, label = 'Skewness: %.2f' % (log.skew()), kde=True)
        axs[0,1].set_title('Log Transformed Data Histogram')
        axs[0,1].legend()
        qqplot(ax=axs[1,1], data=log, scale = 1 ,line = 'q', fit=True)
        axs[1,1].set_title('Log Transformed Data Q-Q Plot')

        # box-cox data
        try:
            boxcox = self.df_name[column_name]
            boxcox= stats.boxcox(boxcox)
            boxcox= pd.Series(boxcox[0])
            sns.histplot(ax=axs[0, 2], data=boxcox, label = 'Skewness: %.2f' % (boxcox.skew()), kde=True)
            axs[0,2].set_title('Box-Cox Data Histogram')
            axs[0,2].legend()
            qqplot(ax=axs[1,2], data=boxcox, scale = 1 ,line = 'q', fit=True)
            axs[1,2].set_title('Box-Cox Data Q-Q Plot')
        except(ValueError):
            print('Box-Cox ValueError: Data must be positive.')

        # yeo-johnson data
        yeojohnson = self.df_name[column_name]
        yeojohnson = stats.yeojohnson(yeojohnson)
        yeojohnson = pd.Series(yeojohnson[0])
        sns.histplot(ax=axs[0, 3], data=yeojohnson, label = 'Skewness: %.2f' % (yeojohnson.skew()), kde=True)
        axs[0,3].set_title('Yeo-Johnson Data Histogram')
        axs[0,3].legend()
        qqplot(ax=axs[1,3], data=yeojohnson, scale = 1 ,line = 'q', fit=True)
        axs[1,3].set_title('Yeo-Johnson Data Q-Q Plot')
        
        # Display the plot
        plt.show()

    def pairplot(self, list_numeric_variables):
        '''
        This method generates scatter plot for each pair of variables in list_numeric_variables. 
        This requires numeric data.
                        
        Parameters:
            df_name (Pandas df): Pandas df
            list_numeric_variables (list of str/object): Names of variables to be analysed

        Returns:
            The pair plot.
        '''
        sns.pairplot(self.df_name[list_numeric_variables])
    
    def count_plot(self, non_numeric_variables):
        '''
        This method generates bar chart for each pair of variables in list_numeric_variables. 
        This requires numeric data.
                        
        Parameters:
            df_name (Pandas df): Pandas df
            list_numeric_variables (list of str/object): Names of variables to be analysed

        Returns:
            The count plot.
        '''
        def countplot(x, **kwargs):
            sns.countplot(x=x)
            x = plt.xticks(rotation=90)
        
        f = pd.melt(self.df_name, value_vars=non_numeric_variables)
        g = sns.FacetGrid(f, col='variable',  col_wrap=3, sharex=False, sharey=False)
        g = g.map(countplot, 'value')

