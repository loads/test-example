import requests
import time


def test():
    for i in range(100):
        requests.get('http://blog.ziade.org/tools.html')
        time.sleep(1.)


if __name__ == '__main__':
    test()
