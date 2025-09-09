import requests, sys
from tabulate import tabulate

ID = "490012553B"

url = f"https://api.tfl.gov.uk/StopPoint/{ID}/Arrivals"

response = requests.get(url)
data = response.json()

# 1. Check for command-line argument or get user input
if len(sys.argv) > 1:
    line_to_filter = sys.argv[1]
else:
    line_to_filter = input("Enter the bus line to filter by: ")

# 2. Filter the departures based on the line ID
departures = []
for dep in data:
    if dep['lineId'].lower() == line_to_filter.lower():
        departures.append([
            dep['lineId'],
            dep['towards'],
            dep['destinationName'],
            dep['expectedArrival']
        ])

headers = ['lineId', 'Towards', 'Destination', 'Arrival Time']
table = tabulate(departures, headers, tablefmt='pretty')

print(table)