import yaml
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

# Function to load credentials.yaml file and return data as a dictionary:
def load_credentials(file_path):
    '''
    Function to load access credentials to AWS remote database from secure yaml file. 
    Returns credentials in dictionary format.
    '''
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

# Class to extract data from remote AWS database:
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
    
    def save_data(self, df):
        try:
            df.to_csv(f'{directory}{table_name}.csv', index=False)
            print('Data saved')
        except:
            print('Saving failed')
    
    def connect_db(self, DATABASE_TYPE, DBAPI, RDS_USER, RDS_PASSWORD, RDS_HOST, RDS_PORT, RDS_DATABASE):
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
    credentials = load_credentials(credentials_file_path)
    connection = RDSDatabaseConnector(credentials)
    connection.connect_db(**credentials)    # Use of the unpacking operator (**) to unpack dictionary into keyword arguments of a function. 

if __name__ == '__main__':
    credentials_file_path = 'C:/Users/Chris/Documents/Career development/AiCore Bootcamp/EDA-Project/credentials.yaml' # Use of forward slash instead of backslash
    table_name = 'customer_activity'
    directory = 'C:/Users/Chris/Documents/Career development/AiCore Bootcamp/EDA-Project/'  # To save df
    load_db(credentials_file_path)





