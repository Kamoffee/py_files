import json
import urllib.request


temperatures = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/12/1850-2023/data.json"

with urllib.request.urlopen(temperatures) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)
