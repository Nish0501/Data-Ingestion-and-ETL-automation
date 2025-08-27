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

etl_automation_project/
├── etl_pipeline.py           # The main Python script (the pipeline orchestrator)
├── config.json               # Metadata file for all configurations
├── last_run.json             # Stores the timestamp for incremental loads
├── users_data.csv            # Output file for the users table
├── orders_incremental.csv    # Output file for the orders table
├── requirements.txt          # Lists all project dependencies
└── README.md                 # Project README file

## 🛠️ How to Run the Pipeline

Follow these steps to set up and run the project:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Nish0501/Data-Ingestion-and-ETL-automation.git](https://github.com/Nish0501/Data-Ingestion-and-ETL-automation.git)
    cd Data-Ingestion-and-ETL-automation
    ```

2.  **Set up the Virtual Environment & Install Dependencies:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    pip install -r requirements.txt
    ```

3.  **Configure the Pipeline:**
    - Open `config.json` and replace the placeholder values with your MySQL credentials and database name.

4.  **Run the Pipeline:**
    ```bash
    python etl_pipeline.py
    ```

The pipeline will execute, and the output CSV files will be generated in the project directory.

---
**Author:** [Nishtha Gupta](https://www.linkedin.com/in/nishthagupta0501)
