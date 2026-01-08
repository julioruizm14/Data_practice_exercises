# ETL Practice Exercise

This is an introductory ETL (Extract, Transform, Load) project in Python, designed to practice data engineering concepts acquired in recent courses.

The script extracts data from multiple file formats (CSV, JSON, XML), transforms the data (standardizing formats and performing calculations), and loads the result into a clean CSV file. It also logs the progress of each stage.

## Prerequisites

* Python
* Pandas library

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/julioruizm14/ETL_easy_practice_exercise.git
    ```

2.  Navigate to the project directory:
    ```bash
    cd ETL_easy_practice_exercise
    ```

3.  Install the required libraries:
    ```bash
    python3 -m pip install pandas
    ```

## Usage

1.  Unzip the data source file:
    ```bash
    unzip datasource.zip
    ```

2.  Execute the Python script:
    ```bash
    python3 etl_code.py
    ```

## Generated Files

After running the script, the following files will be generated in the project directory:

* **transformed_data.csv**: This file contains the final processed data, ready to be loaded into a database.
* **log_file.txt**: This text file contains the timestamped logs of the ETL process (e.g., when extraction started, when transformation ended).
