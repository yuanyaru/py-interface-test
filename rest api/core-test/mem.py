import requests
import json
import time
from leader import get_time

URL = 'http://192.168.100.61:18080/countmem'


def mem():
    while True:
        response = requests.get(URL)
        dsm = json.loads(response.text)
        foo = dsm['foo']
        hello = dsm['hello']
        print str(foo) + "-" + get_time() + "---" + str(hello) + "-" + get_time()
        time.sleep(1)


if __name__ == '__main__':
    mem()