# Data sciencie exercices
These are a set of exercices designed to practice data engineering concepts acquired in recent courses.

## ETL exercise 1: `etl_code.py`

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
    cd Data_practice_exercises
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

## ETL exercise 2: `etl_project_gdp.py`

Second ETL  project in Python with the next objetive:

1. Write a data extraction function to retrieve the relevant information from [the required URL]('https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29').
2. Transform the available GDP information into 'Billion USD' from 'Million USD'.
3. Load the transformed information to the required CSV file and as a database file.
4. Run the required query on the database.
5. Log the progress of the code with appropriate timestamps.

### Libraries
- requests - The library used for accessing the information from the URL.
- bs4 - The library containing the BeautifulSoup function used for webscraping.
- pandas - The library used for processing the extracted data, storing it to required formats and communicating with the databases.
- sqlite3 - The library required to create a database server connection.
- numpy - The library required for the mathematical rounding operation as required in the objectives.
- datetime - The library containing the function datetime used for extracting the timestamp for logging purposes.


### Generated Files

After running the script, the following files will be generated in the directory:

* **Countries_by_GDP.csv**: A CSV file containing the final processed list of countries and their GDP in Billions USD.
* **World_Economies.db**: A SQLite database containing the table `Countries_by_GDP`.
* **etl_project_log.txt**: A text file recording the timestamped progress of the ETL operations (e.g., extraction complete, transformation started).




## Web scraping exercise 1

This script performs web scraping to extract information about the top 50 highly-ranked films from a web archive. It uses the `BeautifulSoup` library to parse HTML content, creates a structured DataFrame, and stores the resulting data in both a CSV file and a SQLite database.

### Libraries
* pandas
* beautifulsoup4
* requests

### Generated Files

After running the script, the following files will be generated in the directory:

* **top_50_films.csv**: A CSV file containing the extracted data for the top 50 films (Rank, Film Name, Year, etc.).
* **Movies.db**: A SQLite database file containing a table named `Top_50` with the scraped data.




## Final proyect: `banks_project.py`

This project performs ETL operations to compile a list of the top 10 largest banks in the world by market capitalization (in Billions USD). The script scrapes data from a web archive, converts the market capitalization into multiple currencies (GBP, EUR, INR) using exchange rate data, and stores the results locally.

### Objectives
1. **Extract** real-world data from a Wikipedia archive URL using Web Scraping.
2. **Transform** the data by converting Market Cap (USD) to GBP, EUR, and INR using exchange rate information from a local CSV file (`exchange_rate.csv`).
3. **Load** the processed data into a CSV file and a SQLite database.
4. **Query** the database to retrieve specific insights (e.g., average market cap in GBP).
5. **Log** the entire process with timestamps.

### Usage

Download exchange_rate.csv and run banks_project.py.

### Libraries
* **requests**: To fetch the HTML content of the webpage.
* **bs4 (BeautifulSoup)**: To parse the HTML and extract table data.
* **pandas**: To manage dataframes, handle CSV I/O, and interact with the database.
* **sqlite3**: To manage the SQL database connection.
* **numpy**: For mathematical operations (rounding).
* **datetime**: For logging timestamps.

### Generated Files
After running the script, the following files will be generated:

* **Largest_banks_data.csv**: A CSV file containing the bank names and their market capitalization in USD, GBP, EUR, and INR.
* **Banks.db**: A SQLite database containing the table `Largest_banks`.
* **code_log.txt**: A text file tracking the progress of the ETL pipeline.
