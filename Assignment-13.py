import requests
import json
resp=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=125634")
#print(resp.status_code)
resps=json.loads(resp.text)
print(resps["quoteText"])
