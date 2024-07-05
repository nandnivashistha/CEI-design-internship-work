#Q6. Write a Python program that writes data to a CSV file using pandas of ISS Location with timestamp (minimum 100 records)

import requests
import pandas as pd

url = "http://api.open-notify.org/iss-now.json"

iss_data = []
for _ in range(100):
    response = requests.get(url)
    data = response.json()
    
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    
    iss_data.append({
        'timestamp': timestamp,
        'latitude': latitude,
        'longitude': longitude
    })

df = pd.DataFrame(iss_data)

df.to_csv('data.csv', index=False)

print("Data written to data.csv")
