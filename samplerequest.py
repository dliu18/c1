# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

apiKey = '3a9ecf6c8c0154fa75bcce7f802a4398'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey);

def numberOfCustomers():
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	customers = response.json();
	return len(customers);

def addCustomer():

	customerData = {
	  "first_name": "A",
	  "last_name": "A",
	  "address": {
	    "street_number": "1",
	    "street_name": "Friend Center",
	    "city": "Princeton",
	    "state": "NJ",
	    "zip": "08544"
	  }
	}

	response = requests.post(
		url,
		data=json.dumps(customerData),
		headers={'content-type':'application/json'},
		)

	return response.json()["objectCreated"]["_id"];

print numberOfCustomers();


# print response.json()["_id"];
# Get merchants
# url = 'http://api.reimaginebanking.com/enterprise/merchants?key={}'.format(apiKey);

# response = requests.get(
# 	url,
# 	headers={'content-type':'application/json'},
# 	)

# result = response.json()["results"];