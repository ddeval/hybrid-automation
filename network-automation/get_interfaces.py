import requests
import os
password = os.environ["ROUTER_PASSWORD"]
url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
headers = {"Accept": "application/yang-data+json"}      # one key, one value
auth = ("cisco", password)

response = requests.get(url, auth=auth, headers=headers, verify=False)

print(response.status_code)
data = response.json()

for interface in data["ietf-interfaces:interfaces"]["interface"]:
    print(f"Interface Name: {interface['name']}")
    print(f"ipv4 Address: {interface['ietf-ip:ipv4']['address'][0]['ip']}")