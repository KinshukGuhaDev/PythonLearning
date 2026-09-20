# An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating a script that can extract the list of the top 10 largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF).

# The required data seems to be available on the URL mentioned below:

# URL: https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29


import pandas as pd
import numpy as np
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(URL)
df = pd.DataFrame(tables[3])
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
country_gdp = df[[0,2]]   
# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
finalData = country_gdp.iloc[1:11,:]

finalData.columns = ['Country', 'IMF-GDP']
print(finalData)

pd.to_csv
