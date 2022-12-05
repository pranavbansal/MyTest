import requests

response = requests.get("https://6363bc2d8a3337d9a2e614ea.mockapi.io/pythonapicalling")
if response.status_code == 200:
    print("successfully fetched the data from the API\n")
    print("Status of the code: ", response, "\n")
    print("Data comes from the api: ", response.content, "\n")
else:
    print("Failed to fetch data from the API")

response01 = requests.get("https://6363bc2d8a3337d9a2e614ea.mockapi.io/pythonapicalling01")
if response01.status_code == 200:
    print("successfully fetched the data from the API", "\n")
    print("Status of the code: ", response01, "\n")
    print("Data comes from the api: ", response01.content, "\n")
else:
    print("Failed to fetch data from the API")
