import yaml
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

# Function to load credentials.yaml file and return data as a dictionary:
def load_credentials(file_path):
    '''
    Function to load access credentials to AWS remote database from secure yaml file. 
    Returns credentials in dictionary format.

    Parameters:
        file_path (str): File path for local .yaml file containing login credentials for AWS RDS. 
    '''
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

# Class to extract data from remote AWS database:
class RDSDatabaseConnector:
    '''
    This class is used to connect to a remote AWS database and retrieve tabular data.

    ------------------
    Parameters:
    credentials: dict
        Dictionary of credentials required to connect to remote RDS.

    ------------------
    Attributes:
    credentials: dict
        Dictionary of credentials required to connect to remote RDS.

    ------------------
    Methods:
    save_data(df)
        Saves df created as .csv file to local directory.
    connect_db(DATABASE_TYPE, DBAPI, RDS_USER, RDS_PASSWORD, RDS_HOST, RDS_PORT, RDS_DATABASE)
        Connects to remote RDS and creates Pandas df from specified table name.
    '''
    def __init__(self, credentials):
        self.credentials = credentials
    
    def save_data(self, df):
        '''
        This method saves the Pandas df to .csv file in specified local directory.

        Parameters:
            df: Pandas DataFrame. 
        '''
        try:
            df.to_csv(f'{directory}{table_name}.csv', index=False)
            print('Data saved')
        except:
            print('Saving failed')
    
    def connect_db(self, DATABASE_TYPE, DBAPI, RDS_USER, RDS_PASSWORD, RDS_HOST, RDS_PORT, RDS_DATABASE):
        '''
        This method connects to the remote RDS and creates a Pandas df of all data from specefied table name.

        Parameters:
            DATABASE_TYPE (str): dialect
            DBAPI (str): driver
            RDS_USER (str): username
            RDS_PASSWORD (str): password
            RDS_HOST (str): host
            RDS_PORT (str): port
            RDS_DATABASE (str): database name
        '''
        try:
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DATABASE}")
            conn = engine.connect()
            print('Connection successful')
        except:
            print('Connection failed')
        df = pd.read_sql(f'SELECT * FROM {table_name}', conn)
        conn.close()
        return self.save_data(df)
        
def load_db(credentials_file_path):
    '''
    This function creates an instance of the class RDSDatabaseConnector and calls the connect_db function to load db using login credentials.

    Parameters:
        credentials_file_path (str): Local file path for .yaml file containing login credentials.
    '''
    credentials = load_credentials(credentials_file_path)
    connection = RDSDatabaseConnector(credentials)
    connection.connect_db(**credentials)    # Use of the unpacking operator (**) to unpack dictionary into keyword arguments of a function. 

if __name__ == '__main__':
    credentials_file_path = 'C:/Users/Chris/Documents/AiCoreEDA_Project/credentials.yaml' # Use of forward slash instead of backslash
    table_name = 'customer_activity'    # Name of table in db, also used to create file_name.
    directory = 'C:/Users/Chris/Documents/AiCoreEDA_Project/EDA-Project/'  # To save df
    load_db(credentials_file_path)





