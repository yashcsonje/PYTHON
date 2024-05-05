#Day 89
#Here is another example that sends a POST request to a web service and includes a custom header:
import requests  # Import the requests module

# Define the URL to which the POST request will be sent
url = "https://jsonplaceholder.typicode.com/posts"

# Define the data to be sent in the request body (JSON format)
data = {
    "title": 'Yash',
    "body": 'bhai',
    "userId": 12,
}

# Define the headers for the request (specifying content type as JSON)
headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

# Send an HTTP POST request to the specified URL with the provided headers and JSON data
response = requests.post(url, headers=headers, json=data)

# Print the response content (JSON data returned by the server)
print(response.text)

'''
Output:
{
  "title": "Yash",
  "body": "bhai",
  "userId": 12,
  "id": 101
}
'''
#The 'requests.post()' function sends an HTTP POST request to the specified URL ('url') with the provided headers ('headers') and JSON data ('data').
#The 'response' object contains the server's response to the request.
#'response.text' prints the content of the response, which typically includes the JSON data returned by the server. In this case, it may include details about the newly created post on the JSONPlaceholder API.