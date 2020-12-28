import requests
import json
url = "https://qrpassservice.azurewebsites.net/module001/checkqr/"
def dump():
	header = {'Content-Type': 'application/json'}
	for i in range(1,100): #While loop thone yan
		finalurl = url+str(i)+"/1"
		resp = requests.post(finalurl, headers = header, data={})
		if ("HTTP Status 500" or "403" or "404") not in resp.text:
			json_dict = json.loads(resp.text)
			company_name = json_dict['Company Name']
dump()