from config import DB_CONFIG, CSV_FILE_PATH_CONFIG
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


# Extracting database connection details from the configuration
dbname = DB_CONFIG['dbname']
user = DB_CONFIG['user']
password = DB_CONFIG['password']
host = DB_CONFIG['host']
port = DB_CONFIG['port']

# get path file csv
csv_file_path = CSV_FILE_PATH_CONFIG['csv_shopping_trends']

# Construct the connection string
connection_string = f"dbname={dbname} user={user} password={password} host={host} port={port}"

# Read CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(connection_string)
    print("Connected to the database!")

    # Create a SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

    # Insert the DataFrame into the database
    df.to_sql('st_details', engine, if_exists='replace', index=False)

    print("Data inserted into PostgreSQL!")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Example: Execute a simple SQL query
    cursor.execute("SELECT count(*) FROM st_details;")
    rows = cursor.fetchall()

    print(rows)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")