class DataTransform():
    '''
    
    '''
    def __init__(self, df_name):
        self.df_name = df_name

    def to_category(self, *args):
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('category')

    def to_datetime(self, *args):
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('timedelta64[ms]')

    def to_Int(self, *args):
        for arg in args:
            self.df_name[arg] = self.df_name[arg].astype('Int64')

    def to_int(self, *args):
            for arg in args:
                self.df_name[arg] = self.df_name[arg].astype('int64')