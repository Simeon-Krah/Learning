#pip install pandas
# import requests
# import pandas as pd
# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
# response=requests.get(filename)
# print('2,3,3,4'.split())
# #print(response.text)
# result=pd.read_csv(filename)
# print(result)
##my way also work without the StringIO. I mean line 8 and 9

import requests
import pandas as pd
from io import StringIO

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
response = requests.get(filename)

if response.status_code == 200:
    data = StringIO(response.text)
    df = pd.read_csv(data)
    print(df)  # Display the first few rows of the DataFrame
else:
    print("Failed to fetch the data")

print(df.iloc[0,1])