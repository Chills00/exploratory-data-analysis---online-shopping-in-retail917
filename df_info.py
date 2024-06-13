class DataFrameInfo():
    '''
    This class is used to generate basic information about a dataframe.

    ------------------
    Parameters:
    df_name: Pandas Dataframe
        Dataset in Pandas Dataframe.

    ------------------
    Attributes:
    df_name: Pandas Dataframe
        Dataset in Pandas Dataframe.

    ------------------
    Methods:
    df_data_type()
        Returns the data type of each column.
    df_stats()
        Returns the descriptive statistics for the df.
    df_category_distinct_values()
        Prints the value counts of unique values for each column containing categorical data.
    df_shape()
        Prints the shape of the df.
    df_null_info()
        Prints the number of null values for each column as a percentage of all values.
    '''
    def __init__(self, df_name):
        self.df_name = df_name

    def df_data_type(self):
        '''
        This method returns the data type of each column.

        Parameters:
            df_name: Pandas Dataframe
        
        Returns:
            The data type of each column.
        '''
        print('The data type for each column is listed below:')
        return self.df_name.dtypes

    def df_stats(self):
        '''
        This method returns the descriptive statistics for the df.

        Parameters:
            df_name: Pandas Dataframe
        
        Returns:
            The statistical summary for each column containing numerical data.
        '''
        print('A statistical summary of the numerical columns is below:')
        return self.df_name.describe()

    def df_category_distinct_values(self):
        '''
        This method prints the value counts of unique values for each column containing categorical data.

        Parameters:
            df_name: Pandas Dataframe
        
        Returns:
            The value counts of unique values for each column containing categorical data.
        '''
        print('The frequency of unique values for each column containing categorical data is below:')
        print()
        data_type_list = self.df_name.dtypes
        for index, data_type in data_type_list.items(): 
            if data_type == 'category':
                print(self.df_name[index].value_counts())
                print()
            else:
                continue
        
    def df_shape(self):
        '''
        This method prints shape of the df.

        Parameters:
            df_name: Pandas Dataframe
        
        Returns:
            The shape of the df, providing the number of columns and number of rows that the dataset has.
        '''
        shape = self.df_name.shape
        return f'The dataset has {shape[0]} columns and {shape[1]} rows.'

    def df_null_info(self):
        '''
        This method prints the number of null values for each column as a percentage of all values.

        Parameters:
            df_name: Pandas Dataframe
        
        Returns:
            The number of null values for each column as a percentage of all values.
        '''
        all_values = len(self.df_name)
        print(f'For any columns containing null values the percentage of null values for that column is:')
        print()
        for column in list(self.df_name):
            sum_missing_values = self.df_name[column].isna().sum()
            percentage = round((100 * sum_missing_values / all_values), 2)
            if percentage > 0:
                print(f'{column} is: {percentage} %')
            else:
                continue
