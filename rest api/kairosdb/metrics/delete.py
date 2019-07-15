#!/usr/bin/python
''' Delete a given metric from KairosDB database using REST API through requests module.
    
    Please, check out the documentation on the KairosDB website:
        http://kairosdb.github.io/docs/build/html/restapi/DeleteMetric.html

    @author yyr
'''

import requests

kairosdb_server = "http://localhost:8080"

# Making the request to KairosDB
metric_name = "test_gzip"
response = requests.delete(kairosdb_server + "/api/v1/metric/" + metric_name)

# Printing the response
print("Status code (204 = Okay): %d" % response.status_code)
