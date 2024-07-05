#Q5. Write a Python program using the requests module to send a GET request to a given URL API endpoint and print the latitude, longitude, and timestamp


import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

data = response.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
timestamp = data['timestamp']

print("Latitude:", latitude)
print("Longitude:", longitude)
print("Timestamp:", timestamp)
