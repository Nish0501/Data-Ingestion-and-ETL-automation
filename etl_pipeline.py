import json
import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine

# A new function to create a SQLAlchemy engine
def create_db_engine(db_config):
    """Creates a SQLAlchemy engine from the database configuration."""
    try:
        engine = create_engine(
            f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database_name']}"
        )
        return engine
    except Exception as e:
        print(f"Error creating SQLAlchemy engine: {e}")
        return None

# 1. Load the configuration from the JSON file
def load_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

# NEW: 2. Function to get the last run timestamp
def get_last_run_time(file_path='last_run.json'):
    """Loads the last run timestamp from a file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get("last_run_timestamp")
    except (FileNotFoundError, json.JSONDecodeError):
        # Return a very old timestamp if file not found
        return "2000-01-01 00:00:00"

# NEW: 3. Function to save the last run timestamp
def save_last_run_time(timestamp, file_path='last_run.json'):
    """Saves the current timestamp to a file for the next run."""
    with open(file_path, 'w') as f:
        json.dump({"last_run_timestamp": timestamp}, f, indent=4)
    print(f"Updated last run timestamp to: {timestamp}")

# 4. Connect to the MySQL database (using SQLAlchemy now)
def connect_to_db(db_engine):
    """Establishes a connection to the MySQL database."""
    conn = None
    try:
        conn = db_engine.connect()
        print("Successfully connected to MySQL database!")
        return conn
    except Exception as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# 5. Function to perform data extraction
def extract_data(conn, query):
    """Executes a query and returns data in a Pandas DataFrame."""
    try:
        # We now use the SQLAlchemy connection object
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        print(f"Error during data extraction: {e}")
        return None

# 6. Function to save data to a CSV file
def save_to_csv(dataframe, filename):
    """Saves a Pandas DataFrame to a CSV file."""
    if dataframe is not None:
        dataframe.to_csv(filename, index=False)
        print(f"Successfully saved data to {filename}")
        print(f"Extracted {len(dataframe)} rows.")

# 7. Main function to orchestrate the pipeline
def run_pipeline():
    config_file = 'config.json'
    config = load_config(config_file)
    print("Configuration loaded successfully!")

    # Create the SQLAlchemy engine
    db_engine = create_db_engine(config['database'])
    if not db_engine:
        return

    db_conn = connect_to_db(db_engine)
    if db_conn:
        try:
            current_run_time = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')

            for table_config in config['tables']:
                table_name = table_config['table_name']
                load_type = table_config['load_type']
                output_file = table_config['output_file']

                if load_type == 'full':
                    query = f"SELECT * FROM {table_name}"
                    print(f"\nPerforming FULL load for table: {table_name}")
                elif load_type == 'incremental':
                    last_run_time = get_last_run_time()
                    incremental_col = table_config['incremental_col']
                    # The actual incremental query
                    query = f"SELECT * FROM {table_name} WHERE {incremental_col} > '{last_run_time}'"
                    print(f"\nPerforming INCREMENTAL load for table: {table_name}")
                    print(f"Querying for records where {incremental_col} > '{last_run_time}'")
                
                df = extract_data(db_conn, query)
                save_to_csv(df, output_file)

            # Save the current timestamp for the next incremental run
            save_last_run_time(current_run_time)

        finally:
            db_conn.close()
            print("\nDatabase connection closed.")

# Entry point of the script
if __name__ == "__main__":
    run_pipeline()