class DataFrameInfo():
    def __init__(self, df_name):
        self.df_name = df_name

    def df_data_type(self):
        print('The data type for each column is listed below:')
        return self.df_name.dtypes

    def df_stats(self):
        print('A statistical summary of the numerical columns is below:')
        return self.df_name.describe()

    def df_category_distinct_values(self):
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
        shape = self.df_name.shape
        return f'The dataset has {shape[0]} columns and {shape[1]} rows.'

    def df_null_info(self):
        all_values = len(self.df_name)
        for column in list(self.df_name):
            sum_missing_values = self.df_name[column].isna().sum()
            percentage = round((100 * sum_missing_values / all_values), 2)
            print(f'The percentage of null values for {column} is: {percentage} %')