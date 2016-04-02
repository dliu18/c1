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

def addMerchant():

	merchantData = {
	  "name": "string",
	  "category": "string",
	  "address": {
	    "street_number": "string",
	    "street_name": "string",
	    "city": "string",
	    "state": "string",
	    "zip": "string"
	  },
	  "geocode": {
	    "lat": 0,
	    "lng": 0
	  }
	}

	response = requests.post(
		url,
		data=json.dumps(merchantData),
		headers={'content-type':'application/json'},
		)

def addPurchase(customer, merchant):
	purchaseData = {
	  "merchant_id": merchant,
	  "medium": "balance",
	  "purchase_date": "2016-04-02",
	  "amount": 0,
	  "status": "pending",
	  "description": "purchase"
	}

	response = requests.post(
		url,
		data=json.dumps(purchaseData),
		headers={'content-type':'application/json'},
		)




# print response.json()["_id"];
# Get merchants
# url = 'http://api.reimaginebanking.com/enterprise/merchants?key={}'.format(apiKey);

# response = requests.get(
# 	url,
# 	headers={'content-type':'application/json'},
# 	)

# result = response.json()["results"];