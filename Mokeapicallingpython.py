import requests


# Method 1
response = requests.get("https://6363bc2d8a3337d9a2e614ea.mockapi.io/pythonapicalling")
print("Status of the code: ", response)
print("Data comes from the api: ", response.content)

if response.status_code == 200:
    print("successfully fetched the data")
else:
    print("Failed to fetch data from the API")

response01 = requests.get("https://6363bc2d8a3337d9a2e614ea.mockapi.io/pythonapicalling01")
print("Status of the code: ", response01)
print("Data comes from the api: ", response01.content)

if response01.status_code == 200:
    print("successfully fetched the data")
else:
    print("Failed to fetch data from the API")
