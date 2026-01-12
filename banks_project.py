# Code for ETL operations on Country-GDP data

# Importing the required libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
import lxml
from datetime import datetime 

# Functions

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the 
    code execution to a log file. Function returns nothing.'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')    


def extract(url, table_attribs):
    ''' This function extracts the required information from the website
    and saves it to a dataframe. The function returns the dataframe for
    further processing. '''
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    

    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr') 

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            anchors = col[1].find_all('a')
            if len(anchors) > 0:
                bank_name = anchors[-1].get_text(strip=True)
            else:
                bank_name = col[1].get_text(strip=True)
            market_cap = col[2].get_text(strip=True)
            data_dict = {"Name": bank_name,
                         "MC_USD_Billion": float(market_cap)}
            
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

    return df


def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    
    exchange_rate = pd.read_csv(csv_path)
    exchange_rate_dict = exchange_rate.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * exchange_rate_dict['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate_dict['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate_dict['INR'], 2) for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''

    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe to as a database table
    with the provided name. Function returns nothing.'''

    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    print(f"\nQuery: {query_statement}")
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
db_name = 'Banks.db'
table_name = 'Largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
csv_path = './Largest_banks_data.csv'
exchange_rate_csv_path = 'exchange_rate.csv' # Assuming you downloaded it to the current folder


log_progress('Preliminaries complete. Initiating ETL process')

# 1. Extraction
df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

# 2. Transformation
# Note: We pass the CSV path for exchange rates here
df = transform(df, exchange_rate_csv_path) 
log_progress('Data transformation complete. Initiating loading process')

# 3. Load to CSV
load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

# 4. Load to Database
sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Executing queries')

# 5. Run Queries
# Query 1: Print the contents of the entire table
query1 = f"SELECT * FROM {table_name}"
run_query(query1, sql_connection)

# Query 2: Print the average market capitalization of all the banks in Billion GBP
query2 = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query2, sql_connection)

# Query 3: Print only the names of the top 5 banks
query3 = f"SELECT Name from {table_name} LIMIT 5"
run_query(query3, sql_connection)

log_progress('Process Complete.')

# 6. Close Connection
sql_connection.close()
log_progress('Server Connection closed.')