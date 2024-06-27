import yaml
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import pandas as pd
import psycopg2

# Function to load credentials.yaml file and return data as a dictionary:
def load_credentials(file_path):
    '''
    Function to load access credentials to AWS remote database from secure yaml file. 
    Returns credentials in dictionary format.

    Parameters:
        file_path (str): File path for local .yaml file containing login credentials for AWS RDS. 

    Returns:
        credentials (dict): Dictionary of login credentials
    '''
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

# Class to extract data from remote AWS database:
class RDSDatabaseConnector:
    '''
    This class is used to connect to a remote AWS database and retrieve tabular data.
    
    ------------------
    Methods:
    save_data()
        Saves df created as .csv file to local directory.
    load_df()
        Creates a df containing all data from specified table.
    connect_db()
        Connects to remote RDS.
    '''
    def save_data(self, df):
        '''
        This method saves the Pandas df to .csv file in specified local directory.

        Parameters:
            df: Pandas DataFrame. 
        
        Returns:
            .csv file containing data.
        '''
        try:
            df.to_csv(f'{directory}{table_name}.csv', index=False)
            print('Data saved')
        except:
            print('Saving failed')
    
    def load_df(self, conn):
        '''
        This method creates a Pandas df from the data in the selected table.

        Parameters:
            conn: Sqlalchemy database conncetion.

        Returns:
            Calls save_data() function with df. 
        '''
        df = pd.read_sql(f'SELECT * FROM {table_name}', conn)
        conn.close()
        return self.save_data(df)
    
    def connect_db(self, credentials_dict):
        '''
        This method connects to the remote RDS. 

        Parameters: 
            credentials_dict (dict): Dictionary of login credentials

        Returns:
            Sqlalchemy connection to remote database.
        '''
        url = URL.create('postgresql+psycopg2', **credentials_dict)
        try:
            engine = create_engine(url, echo=True)
            conn = engine.connect()
            print('Connection successful')
        except:
            print('Connection failed')
        return self.load_df(conn)
        
def load_db(credentials_file_path):
    '''
    This function creates an instance of the class RDSDatabaseConnector and calls the connect_db function to load db using login credentials.

    Parameters:
        credentials_file_path (str): Local file path for .yaml file containing login credentials.

    Returns:
        Calls connect_db() function with credentials dictionary. 
    '''
    credentials = load_credentials(credentials_file_path)
    connection = RDSDatabaseConnector()
    connection.connect_db(credentials) 

if __name__ == '__main__':
    credentials_file_path = 'C:/Users/Chris/Documents/AiCoreEDA_Project/credentials.yaml' # Use of forward slash instead of backslash
    table_name = 'customer_activity'    # Name of table in db, also used to create file_name.
    directory = 'C:/Users/Chris/Documents/AiCoreEDA_Project/'  # To save df C:\Users\Chris\Documents\AiCoreEDA_Project\customer_activity_transformed.csv
    load_db(credentials_file_path)
