#!/usr/bin/python
''' List metrics from KairosDB database using REST API through requests module.
    
    Please, check out the documentation on the KairosDB website:
        http://kairosdb.github.io/docs/build/html/restapi/ListMetricNames.html

    @author yyr
'''

import requests, json

kairosdb_server = "http://localhost:8080"

# Making the request to KairosDB, Returns a list of all metric names.
response = requests.get(kairosdb_server + "/api/v1/metricnames")
# Printing the response
print(json.dumps(response.json()))

# If you specify the prefix parameter, only names that start with prefix are returned.
response = requests.get(kairosdb_server + "/api/v1/metricnames?prefix=test")
print(json.dumps(response.json()))
