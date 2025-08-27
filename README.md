# Data Ingestion & ETL Automation Pipeline

This project is a robust, metadata-driven ETL pipeline built in Python. It's designed to automate the process of extracting data from a MySQL database, transforming it, and loading it into a CSV file. The pipeline is highly efficient and scalable, capable of handling both full and incremental data loads.

## 🚀 Key Features

- **Metadata-Driven ETL:** The pipeline's behavior is controlled by a simple `config.json` file. This allows for dynamic extraction, making the pipeline reusable and easy to manage without changing the core code.
- **Full & Incremental Loads:** Efficiently handles different data scenarios:
  - **Full Load:** Fetches the entire dataset for initial or complete data refreshes.
  - **Incremental Load:** Smarter extraction that only pulls new or updated records since the last run, significantly improving efficiency for large datasets.
- **Automated Workflow:** The entire process is automated, from database connection to file saving, which drastically reduces manual effort and the potential for human error.
- **Parameterized & Reusable:** The database, table, and load configurations are all parameterized in the `config.json` file, allowing the same pipeline to be used across multiple data sources.

## ⚙️ Technologies Used

- **Python:** The core programming language for the pipeline's logic.
- **Pandas:** Used for efficient data processing, transformation, and saving to CSV files.
- **MySQL:** The relational database serving as the data source.
- **SQLAlchemy:** Used for reliable and robust database connectivity.

## 📂 Project Structure

The project is structured for clarity and easy navigation:
