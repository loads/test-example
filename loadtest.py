import requests
import time
import sys


def test():
    for i in range(10):
        requests.get('http://blog.ziade.org/tools.html')
        time.sleep(.1)
        sys.stdout.write('.')
        sys.stdout.flush()


if __name__ == '__main__':
    test()
