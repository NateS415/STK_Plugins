import requests
import json
import pandas as pd
import time
from datetime import datetime

observer_lat = 39.397
observer_lng = -77.4365
observer_alt = 0
search_radius = 25
category_id = 52
API_KEY = "YPUN92-B9S9SB-QDDNRQ-5ACW"

# Replace with the API endpoint you want to call
API_URL = f'https://api.n2yo.com/rest/v1/satellite/above/{observer_lat}/{observer_lng}/{observer_alt}/{search_radius}/{category_id}/&apiKey={API_KEY}'

def main_loop():
    while True:
        response = requests.get(API_URL)
        df = pd.json_normalize(json.loads(response.content.decode('utf-8')), 'above')
        satid = df['satid']

        now = datetime.now()

        print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
        print(list(satid))

        time.sleep(2.5)

if __name__ == "__main__":
    main_loop()