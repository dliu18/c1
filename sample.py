# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

apiKey = 'c63b87f65e5d2818d5037b9a8f42ab35'

page = 1;
geocodes = [];

while True: 
	url = 'http://api.reimaginebanking.com/atms?key={}&page={}'.format(apiKey, str(page))
	response = requests.get( 
		url, 
		headers={'Accept':'application/json'},
	)
	results = response.json()["data"]	

	if len(results) == 0:
		break;

	for item in results:
		geocodes.append(item["geocode"])

	page += 1

output = {}
output["ATMS"] = geocodes

print json.dumps(output, indent=4, separators=(',', ': '))
