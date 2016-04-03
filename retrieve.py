#Get all customers 
#Get the customer's account id 
#Get all of the purchases
#Continue if more than 1 purchase
#Loop through all merchants and count frequencies 

import requests
import json

apiKey = '55a07fa3a0c50cb8eb774360f1ddb74e'

def getCustomers():
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	customers = response.json()
	return customers

def getAccountID(customer):
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer, apiKey)
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	accounts = response.json()
	if len(accounts) != 1:
		return 0
	return accounts[0]["_id"]

def getPurchases(account):
	url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(account, apiKey)
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	purchases = response.json()
	return purchases

def getMerchantName(merchantID):
	url = 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(merchantID, apiKey)
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	merchant = response.json()
	return merchant["name"]

def getPurchasesMerchant(merchantID):
	url = 'http://api.reimaginebanking.com/merchants/{}/purchases?key={}'.format(merchantID, apiKey)
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	purchases = response.json()
	return purchases

def getMerchants():
	url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey)
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	merchants = response.json()
	return merchants

def main1():
	dictionary = {}
	customers = getCustomers()
	merchantDictionary = {} #id to name
	customerDictionary = {} #id to name
	for customer in customers:
		account = getAccountID(customer["_id"])
		if account == 0:
			continue
		customerDictionary[customer["_id"]] = customer["first_name"] + " " + customer["last_name"] 
		merchantMap = {}
		purchases = getPurchases(account)
		if (len(purchases) == 0): continue
		for purchase in purchases:
			merchant = purchase["merchant_id"]
			merchants = merchantMap.keys()
			if merchant not in merchants:
				merchantMap[merchant] = 0
				keys = merchantDictionary.keys()
				if merchant not in keys:
					merchantDictionary[merchant] = getMerchantName(merchant)
			merchantMap[merchant] += 1
		dictionary[customer["_id"]] = merchantMap
	return merchantDictionary

def main2():
	dictionary = {}
	customers = getCustomers()
	for customer in customers:
		account = getAccountID(customer["_id"])
		if account == 0:
			continue
		purchases = getPurchases(account)
		if (len(purchases) == 0): continue
		for purchase in purchases:
			merchant = purchase["merchant_id"]
			merchants = dictionary.keys()
			if merchant not in merchants:
				dictionary[merchant] = {}
			keys = dictionary[merchant]
			if customer["_id"] not in keys:
				dictionary[merchant][customer["_id"]] = 0
			dictionary[merchant][customer["_id"]] += 1
	return dictionary

dictionary = main1()
print json.dumps(dictionary, indent=4, separators=(',', ': '))

