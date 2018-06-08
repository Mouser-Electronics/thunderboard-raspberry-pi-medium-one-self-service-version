from bluepy.btle import *


def scan():
    scanner = Scanner(0)
    devices = scanner.scan(3) # List of ScanEntry objects
    while True:
        scanner = Scanner(0)
        devices = scanner.scan(3)  # List of ScanEntry objects
        for dev in devices:
            for (adtype, desc, value) in dev.getScanData():
                if "Thunder Sense" in value:
                    print("addr {}, addrtype {}, value {}".format(dev.addr, dev.addrType, value))


scan()
