import speedtest
import requests
import pprint
from config import SERVERS, URL, HEADERS, CUSTOMER_NAME
from addict import Dict

pp = pprint.PrettyPrinter(indent=4)

s = speedtest.Speedtest()

# if you run this get_best_server without a server_list it will select one for you bast on proximity and latency
s.get_best_server(SERVERS)

# run download /upload tests
s.download()
s.upload()
# set results
results = Dict(s.results.dict())
results.client.customer_name = CUSTOMER_NAME
# post the results to an end-point of your choice.
pp.pprint(results)
response = requests.request('POST', url=URL, headers=HEADERS, json=results)
print(response.text)