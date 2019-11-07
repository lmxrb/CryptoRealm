import requests
import json
 
#id                     Id
#rank                   Rank is in ascending order - this number is directly associated with the marketcap whereas the highest marketcap receives rank 1
#symbol                 Most common Symbol
#name                   Proper Name
#supply                 Available supply for trading
#maxSupply              Total quantity of asset issued
#marketCapUsd           Supply x Price
#volumeUsd24Hr          Quantity of trading volume represented in USD over the last 24 hours
#priceUsd               Volume-weighted price based on real-time market data, translated to USD
#changePercent24Hr      The direction and value change in the last 24 hours
#vwap24Hr               Volume Weighted Average Price in the last 24 hours
 
 
def request():
    url = 'https://api.coincap.io/v2/assets/'
    payload = {}
    headers = {}
    return requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout = 5).text
 
 
def updateDB(data):
    if (data):
        file = open("btc.json5", "w+")
        file.write(data)
        file.close()
        return json.load(open("btc.json5", "r"))
    else:
        print("Something went wrong and no data was collected to the database.")
 
def searchDBint(id):
    filedict = updateDB(request())
    if(id <= 99 and id >= 0):
        return filedict["data"][id]
    else:
        return 0

#TODO: Maybe unused?
#def searchDBid(name):
 #   filedict = updateDB(request())
  #  for id in range(100):
   #     if filedict["data"][id]["id"] == name:
    #        return searchDBint(id)

def returnNames():
    names = []
    filedict = updateDB(request())
    for id in range(100):
        names.append(filedict["data"][id]["name"])
    return names


def price(data):
    return data["priceUsd"].split('.')[0] + "." + data["priceUsd"].split('.')[1][:4]


def pricechange(data):
 	return data["changePercent24Hr"].split('.')[0] + "." + data["changePercent24Hr"].split('.')[1][:2]


def traded24hr(data):
	return data["volumeUsd24Hr"].split('.')[0] + "." + data["volumeUsd24Hr"].split('.')[1][:2]


def supply(data):
    return data["supply"].split('.')[0]


#TODO: Don't forget that the currency in the top 100 can change and some might become unavailable... Find an alternative around that.
#TODO: Get only individual data for each currency (maybe using a for loop or something)
