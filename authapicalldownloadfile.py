import requests

# Method 1 with Token and username atlassian jira

# Jira account api token "oNCSluaFJDmlFhpDwMcnA0BB"
# api_token = 'oNCSluaFJDmlFhpDwMcnA0BB'
# response = requests.get("https://pentair.atlassian.net/", auth=("pranav.bansal@pentair.com", api_token))
# print(response)
# print(response.content)

# Method 2 with Username and Password atlassian jira

url = 'https://pentair.atlassian.net/'
values = {'username': 'pranav.bansal@pentair.com',
          'password': 'einfochips@123'}
response = requests.get(url, data=values)
print(response)
# print(response.content)
