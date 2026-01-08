# Data sciencie exercices
These are a set of exercices designed to practice data engineering concepts acquired in recent courses.

## ETL Practice Exercise

This is an introductory ETL (Extract, Transform, Load) project in Python, designed to practice data engineering concepts acquired in recent courses.

The script extracts data from multiple file formats (CSV, JSON, XML), transforms the data (standardizing formats and performing calculations), and loads the result into a clean CSV file. It also logs the progress of each stage.

### Prerequisites

* Python
* Pandas library

### Usage

1.  Clone the repository:
    ```bash
    git clone https://github.com/julioruizm14/Data_practice_exercise.git
    ```

2.  Navigate to the project directory:
    ```bash
    cd Data_practice_exercises/ETL_easy
    ```

3.  Download source data:
    ```bash
    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip 
    ```

4.  Install the required libraries:
    ```bash
    python3 -m pip install pandas
    ```

5.  Execute the Python script:
    ```bash
    python3 etl_code.py
    ```

### Generated Files    
After running the script, the following files will be generated in the  directory:

* **transformed_data.csv**: This file contains the final processed data, ready to be loaded into a database.
* **log_file.txt**: This text file contains the timestamped logs of the ETL process (e.g., when extraction started, when transformation ended).

## Web scraping

This script performs web scraping to extract information about the top 50 highly-ranked films from a web archive. It uses the `BeautifulSoup` library to parse HTML content, creates a structured DataFrame, and stores the resulting data in both a CSV file and a SQLite database.

### Prerequisites

* Python
* Libraries: `pandas`, `beautifulsoup4`, `requests`

### Usage

1.  Navigate to the project directory:
    ```bash
    cd Data_practice_exercises/Web_scraping
    ```

2.  Install the required libraries:
    ```bash
    python3 -m pip install pandas beautifulsoup4 requests
    ```

3.  Execute the Python script:
    ```bash
    python3 web_scraping.py
    ```

### Generated Files

After running the script, the following files will be generated in the directory:

* **top_50_films.csv**: A CSV file containing the extracted data for the top 50 films (Rank, Film Name, Year, etc.).
* **Movies.db**: A SQLite database file containing a table named `Top_50` with the scraped data.


