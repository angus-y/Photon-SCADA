import socket
import requests
import modules.config as config

config.main()


def main():
    while True:
        try:
            data = requests.get('http://blynk-cloud.com/PibLh_9lhMCt_5fmc17ftsDfMWkqdx0S/get/V7')
            config.blynk_val = float(data.text[2:][:-2])
        except socket.gaierror:
            return
        except ValueError:
            print('\x1b[1m\x1b[33m[-]\x1b[0mBlynk server is not streaming data')
