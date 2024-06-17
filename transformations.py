import pandas as pd
import numpy as np

class DataTransform():
    '''
    This class is used to change the data type of specified column(s) to a new data type.

    ------------------
    Parameters:
    df_name: Pandas df
        A Pandas dataframe

    ------------------
    Attributes:
    *args: Column header(s)
        Any number of columns

    ------------------
    Methods:
    to_category()
        Converts the specified column(s) to category data type.
    to_datetime()
        Converts the specified column(s) to datetime64 data type.
    to_Int()
        Converts the specified column(s) to Int64 data type.
    to_int()
        Converts the specified column(s) to int64 data type.
    to_total_seconds()
        Converts the specified column(s) from timedelta to float64 data type.
    '''
    def __init__(self, df_name):
        self.df_name = df_name

    def to_category(self, *args):
        '''
        This method converts the specified column(s) to category data type.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            The specified column(s) as category.
        '''  
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('category')

    def to_datetime(self, *args):
        '''
        This method converts the specified column(s) to datetime64 data type.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            The specified column(s) as datetime64 to the millisecond value.
        '''  
        for arg in args:
            self.df_name[arg] = pd.to_timedelta(self.df_name[arg], unit='s')

    def to_Int(self, *args):
        '''
        This method converts the specified column(s) to Int64 data type.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            The specified column(s) as Int64.
        '''  
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('Int64')

    def to_int(self, *args):
        '''
        This method converts the specified column(s) to int64 data type.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            The specified column(s) as int64.
        '''    
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('int64')
    
    def to_total_seconds(self, *args):
        '''
        This method convert timedelta values in the specified column(s) to a float value representing total seconds.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            The specified column(s) as float64.
        '''   
        for arg in args:
            self.df_name[arg] = self.df_name[arg].dt.total_seconds()

class DataFrameTransform():
    '''
    This class is used to change the dataframe (df).

    ------------------
    Parameters:
    df_name: Pandas df
        A Pandas dataframe

    ------------------
    Attributes:
    column_name: Column header
        Column to be transformed
    *args: Column header(s)
        Any number of columns

    ------------------
    Methods:
    drop_columns()
        Drops specified columns from df.
    drop_rows_from_columns()
        Drops rows by searching specified columns for null-values. 
    drop_negative_rows()
        Drops rows by searching specified columns for negative-values. 
    drop_all_nulls()
        Drops all rows if null-value is in df.
    impute_mean()
        Imputes null-values in specified column with mean value.
    impute_median()
        Imputes null-values in specified column with median value.
    impute_mode()
        Imputes null-values in specified column with mode value.
    log_transformation()
        Transforms the data using the Log transform method. 
    '''
    def __init__(self, df_name):
        self.df_name = df_name
    
    def drop_columns(self, *args):  # arg is column_name
        '''
        This method drops specified columns from df.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            A df with specified columns removed.
        '''    
        list_column_names = []
        for arg in args:
            list_column_names.append(arg)
        return self.df_name.drop(list_column_names, axis=1)

    def drop_rows_from_columns(self, *args):    # arg is column_name
        '''
        This method takes in column_name(s) as a parameter and searches within those column(s) for null-values. If found, those rows are dropped.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            A df with null-values removed from specified columns.
        '''   
        list_column_names = []
        for arg in args:
            list_column_names.append(arg)
        return self.df_name.dropna(subset=list_column_names)
    
    def drop_negative_rows(self, *args):
        '''
        This method takes in column_name(s) as a parameter and searches within those column(s) for negative-values. If found, those rows are dropped.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            A df with negative-values removed from specified columns.
        '''   
        for arg in args:
            self.df_name.drop(self.df_name[self.df_name[arg] < 0].index, inplace=True)
        return self.df_name
        
    def drop_all_nulls(self):
        '''
        This method removes all rows within a df if a null-value is found in that row.

        Parameters:
            df_name (Pandas df): Pandas df
            *args (str): Column header(s)
        
        Returns:
            A df with null-values removed from specified columns.
        ''' 
        return self.df_name.dropna(axis=0, how='any', thresh=0) # threshold can be increased if needed
    
    def impute_mean(self, column_name):
        '''
        This method imputes all null-values in specified column with mean value.

        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Column header
        
        Returns:
            A df with null-values imputed with the mean value for the specified columns.
        ''' 
        return self.df_name[column_name].fillna(self.df_name[column_name].mean())
                    
    def impute_median(self, column_name):
        '''
        This method imputes all null-values in specified column with median value.

        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Column header
        
        Returns:
            A df with null-values imputed with the median value for the specified columns.
        ''' 
        return self.df_name[column_name].fillna(self.df_name[column_name].median())
            
    def impute_mode(self, column_name):
        '''
        This method imputes all null-values in specified column with mode value.

        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Column header
        
        Returns:
            A df with null-values imputed with the mode value for the specified columns.
        ''' 
        return self.df_name.fillna({column_name: self.df_name[column_name].mode()[0]})
    
    def log_transformation(self, *args):
        '''
        This method transforms the data using the Log transform method. 
        The transformation involves replacing each value x with log(x) (except from 0).
                
        Parameters:
            df_name (Pandas df): Pandas df
            column_name (str/object): Name of variable to be analysed

        Returns:
            The histogram and Q-Q plot.
        '''
        for arg in args:
            self.df_name[arg] = self.df_name[arg].map(lambda i: np.log(i) if i > 0 else 0)
        return self.df_name
    
    def replace_categories(self, column_name, list_category_to_replace, replacement_category):
        self.df_name[column_name] = self.df_name[column_name].replace(list_category_to_replace, replacement_category)
        return self.df_name[column_name].value_counts()
