import json
import requests
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
content = requests.get(URL)
# path = os.path.join(os.getcwd(), 'Example.txt')
# with open(path, 'wb') as file:
#     file.write(content.content)
result = json.loads(content.text)
print(result)