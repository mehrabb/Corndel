import requests
from flask import Flask
from tabulate import tabulate

app = Flask(__name__)

ID = "490012553B"

# Remove the API call from here.
# url = f"https://api.tfl.gov.uk/StopPoint/{ID}/Arrivals"
# response = requests.get(url)
# data = response.json()

# Hardcode the bus line for now to avoid the input() issue.
line_to_filter = "214"

@app.route("/")
def dep():
    url = f"https://api.tfl.gov.uk/StopPoint/{ID}/Arrivals"
    response = requests.get(url)
    data = response.json()

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

    return f'<pre>{table}</pre>' # Use <pre> tags to preserve formatting