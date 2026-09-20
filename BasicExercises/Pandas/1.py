import pandas as pd

dataframe_list = {
    "id": [1,2,3,4,5],
    "first_name": ["andrew", "john", "jane", "mike", "sara"],
    "last_name": ["smith", "doe", "doe", "johnson", "williams"],
    "email": ["andrew.smith@example.com", "john.doe@example.com", "jane.doe@example.com", "mike.johnson@example.com", "sara.williams@example.com"],
    "gender": ["Male", "Male", "Female", "Male", "Female"],
    "age": [25, 30, 28, 35, 22],
    "country": ["USA", "USA", "Canada", "USA", "Canada"],
    "salary": [50000, 60000, 55000, 70000, 48000]
}

df = pd.DataFrame(dataframe_list)
# df.to_excel("Assets/data.xlsx")
print(df['first_name'])