# !/usr/bin/python
# encoding:utf-8

import sys
import traceback
import Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea

ic = None
status = 0


def ice_con():
    status = 0
    try:
        ic = Ice.initialize(sys.argv)
        base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
        DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
        # print(type(DataCommand))
        if not DataCommand:
            raise RuntimeError("Invalid proxy")
        else:
            print("哇！！！恭喜你已经连上ICE!")
            return DataCommand
    except:
        traceback.print_exc()
        status = 1
    sys.exit(status)


def destroy():
    if ic:
        try:
            ic.destroy()
        except:
            traceback.print_exc()
            status = 1
    sys.exit(status)


if __name__ == '__main__':
    ice_con()
    destroy()