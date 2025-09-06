import requests
from tabulate import tabulate

url = "https://transportapi.com/v3/uk/train/station_timetables/crs:WTN.json"

headers = {
    'X-App-Id': 'd103c1d0',
    'X-App-Key': 'dd7c385558ce066c37ad588ad786f8f7'
}

result = requests.get(url, headers=headers)
data = result.json()

departures = []
for departure in data['departures']['all']:
    departures.append([
        departure['aimed_departure_time'],
        departure['platform'],
        departure['destination_name']
    ])

headers = ['Departure Time', 'Platform', 'Destination']
table = tabulate(departures, headers, tablefmt='pretty')

print(table)