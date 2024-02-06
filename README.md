# API Scraper Example

This Python script is designed to scrape Tesla car data from the Autolist API and store it in an Excel file. The script utilizes the `requests` library for making HTTP requests and `pandas` for data manipulation.

## Usage

1. **Dependencies:**
   - Make sure you have the required libraries installed. You can install them using the following command:
     ```
     pip install requests pandas
     ```

2. **Run the Script:**
   - Execute the Python script `api_scraper.py`.

3. **Output:**
   - The script will fetch Tesla car data from the Autolist API, including model, mileage, year, dealer name, and price.
   - The extracted data will be saved in an Excel file named `tesla.xlsx`.

## Code Explanation

- `import requests`: Importing the library for making HTTP requests.
- `import pandas as pd`: Importing the library for data manipulation and analysis.

- `headers`: Setting headers to mimic a web browser for the HTTP request.

- Initializing empty lists (`model`, `mileage`, `year`, `dealer_name`, `price`) to store data extracted from the API.

- Looping through pages 1 to 5 to fetch car data from Autolist API:
  - Defining parameters for the API request (`params`).
  - Making an HTTP GET request to the Autolist API.
  - Parsing the JSON response.
  - Extracting the list of car records from the response.

- Looping through each car record and extracting relevant information:
  - Appending data (model, mileage, year, dealer name, price) to respective lists.

- Creating a pandas DataFrame (`tesla_df`) from the extracted data.

- Writing the DataFrame to an Excel file (`tesla.xlsx`).
