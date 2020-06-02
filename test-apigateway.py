#Test an API Gateway Trigger:
# Be sure to install dependencies before hand: `pip install requests`
import requests
url = "https://3hvesyht1h.execute-api.us-west-2.amazonaws.com/default/cloud9-checkwikipedia-checkwikipedia-1PZJVADH3KHAM"
result = requests.post(url, json={"entity": "google"})
result.json()
