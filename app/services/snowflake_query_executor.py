import snowflake.connector
import os
import pandas as pd
import time
from dotenv import load_dotenv  

load_dotenv()

class SnowflakeQueryExecutor:
    def __init__(self, user, password, account, warehouse, database, schema):
        self.user = user
        self.password = password
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.conn = self.create_connection()
    
    def create_connection(self):
        return snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )
    
    def execute_query_from_file(self, sql_query_file_path):
        # Read the SQL query from the file
        with open(sql_query_file_path, 'r') as file:
            sql_query = file.read()
        
        cursor = self.conn.cursor()
        tic = time.time()
        try:
            cursor.execute(sql_query)
            results = cursor.fetchall()
            # Extract column names from cursor.description
            columns = [desc[0] for desc in cursor.description]
        except Exception as e:
            print(f"An error occurred: {e}")
            results = []
            columns = []
        toc = time.time()
        print(f"Query executed in {toc - tic} seconds")
        
        # Create and return a DataFrame with the results and column names
        df = pd.DataFrame(results, columns=columns)
        cursor.close()
        return df
    
    def close(self):
        self.conn.close()
