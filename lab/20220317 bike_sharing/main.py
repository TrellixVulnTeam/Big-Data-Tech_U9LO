import datetime
import requests
import json

url = "https://os.smartcommunitylab.it/core.mobility/bikesharing/trento"

payload = ""
response = requests.request("GET", url, data=payload)


bike_stations = json.loads(response.text)



##### Total slots #####
tot_slots = 0
for idx, station in enumerate(bike_stations):
    tot_slots += station["totalSlots"]

print(tot_slots)

# alternative #
total_slots_list = [station["totalSlots"] for station in bike_stations]

print(sum(total_slots_list))


##### Add city and ts to each entry #####

current_ts = datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
current_city = url.split("/")[-1]

for station in bike_stations:
    station["city"] = current_city
    # alternative
    #station["city"] = station["id"].split(" - ")[1]

    station["timestamp"] = current_ts

print(bike_stations[70])

with open(f"stations_{current_city}.json", "w") as f:
    json.dump(bike_stations, f, indent=2)