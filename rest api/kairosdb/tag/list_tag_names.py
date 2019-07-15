#!/usr/bin/python
''' List tag names from KairosDB database using REST API through requests module.
    
    Please, check out the documentation on the KairosDB website:
        http://kairosdb.github.io/docs/build/html/restapi/ListTagNames.html

    @author yyr
'''

import requests, json

kairosdb_server = "http://localhost:8080"

# Making the request to KairosDB
response = requests.get(kairosdb_server + "/api/v1/tagnames")

# Printing the response
print(json.dumps(response.json()))
