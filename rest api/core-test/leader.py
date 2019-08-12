import requests
import json
import time

URL = 'http://192.168.100.63:18080/leader'


def get_time():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp


def leader():
    while True:
        response = requests.get(URL)
        lead = json.loads(response.text)
        lead_ip = lead['Leader']
        node = lead_ip[12:14]
        print node + "---" + get_time()


if __name__ == '__main__':
    leader()