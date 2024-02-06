# Importing necessary libraries
import requests # Library for making HTTP requests
import pandas as pd # Library for data manipulation and analysis

# Defining headers for the HTTP request to mimic a web browser
headers = {
    'sec-ch-ua': '^\\^Not',
    'Referer': 'https://www.autolist.com/listings',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
}

# Initializing empty lists to store data extracted from the API
model=[]
mileage=[]
year=[]
dealer_name=[]
price=[]

# Looping through pages 1 to 5 to fetch car data from Autolist API
for i in range(1,6):

    # Defining parameters for the API request
    params = (
        ('ads', 'true'),
        ('include_total_price_change', 'true'),
        ('include_time_on_market', 'true'),
        ('include_relative_price_difference', 'true'),
        ('latitude', '37.7749295'),
        ('limit', '20'),
        ('longitude', '-122.4194155'),
        ('make', 'Tesla'),
        ('page', str(i)),
        ('radius', '100'),
        ('zip', ''),
    )

    # Making an HTTP GET request to the Autolist API
    response = requests.get('https://www.autolist.com/api/v2/search', headers=headers, params=params)
    # Parsing the JSON response
    results_json = response.json()
    # Extracting the list of car records from the response
    result_items = results_json['records']

     # Looping through each car record and extracting relevant information
    for result in result_items:
        model.append(result['model_name'])
        mileage.append(result['mileage'])
        year.append(result['year'])
        dealer_name.append(result['dealer_name'])
        price.append(result['price'])

# Creating a pandas DataFrame from the extracted data
tesla_df = pd.DataFrame({'Model':model, 'Mileage':mileage, 'Year':year, 'Dealer Name':dealer_name, 'Price':price})

# Writing the DataFrame to an Excel file named 'tesla.xlsx'
tesla_df.to_excel('tesla.xlsx', index=False)