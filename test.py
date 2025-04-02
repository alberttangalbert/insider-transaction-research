import snowflake.connector
import os 
import pandas as pd
import time
from dotenv import load_dotenv  

load_dotenv()

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    account=os.getenv('ACCOUNT'),
    warehouse=os.getenv('WAREHOUSE'),
    database=os.getenv('DATABASE'),
    schema=os.getenv('SCHEMA')
)

# Read the SQL query from the file
sql_query_file_path = "sql/fetch_ndt.sql"
with open(sql_query_file_path, 'r') as file:
    sql_query = file.read()

# Execute the SQL query
tic = time.time()
cursor = conn.cursor()
try:
    cursor.execute(sql_query)
    
    # Fetch all results
    results = cursor.fetchall()
except Exception as e:
    print(f"An error occurred: {e}")
toc = time.time()

# Export the results to a CSV file
df = pd.DataFrame(results)
df.to_csv('output.csv', index=False, header=False)

# Close the cursor and connection
cursor.close()
conn.close()

print("Data exported to output.csv in", toc - tic, "seconds")

