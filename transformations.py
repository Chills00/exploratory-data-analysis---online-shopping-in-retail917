class DataTransform():
    '''
    This class is used to change the data type of specified column(s) to a new data type.

    ------------------
    Parameters:
    *args: Column header(s)
        Any number of columns

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
    '''
    def __init__(self, df_name):
        self.df_name = df_name

    def to_category(self, *args):
        '''
        This method converts the specified column(s) to category data type.

        Parameters:
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
            *args (str): Column header(s)
        
        Returns:
            The specified column(s) as datetime64 to the millisecond value.
        '''  
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('timedelta64[ms]')

    def to_Int(self, *args):
        '''
        This method converts the specified column(s) to Int64 data type.

        Parameters:
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
            *args (str): Column header(s)
        
        Returns:
            The specified column(s) as int64.
        '''    
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('int64')