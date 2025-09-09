import requests
from tabulate import tabulate

ID = "490012553B"

url = f"https://api.tfl.gov.uk/StopPoint/{ID}/Arrivals"

response = requests.get(url)
data = response.json()

departures = []
for dep in data:
    departures.append([
        dep['lineId'],
        dep['towards'],
        dep['destinationName'],
        dep['expectedArrival']
    ])

headers = ['lineId', 'Towards', 'Destination', 'Arrival Time']
table = tabulate(departures, headers, tablefmt='pretty')

print(table)