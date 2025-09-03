import requests

LAT = 51.5
LON = -0.11
CITY = "London"

url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=precipitation&forecast_days=1"

response = requests.get(url)
data = response.json()

will_rain = False
for precip in data["hourly"]["precipitation"][:8]:
    if precip > 0:
        will_rain = True
        break

if will_rain:
    #print("Rain expected today, bring an umbrella!")
    print(f"Rain expected today in the next 8 hours in {CITY}, bring an umbrella!")
else:
    #print("No rain forecast, have a wonderful day!")
    print(f"No rain forecast today in the next 8 hours in {CITY}, have a wonderful day!")

print("Welcome to the Weather App!")
#print(data)
#print(f"Will it rain in the next 8 hours? {will_rain}")