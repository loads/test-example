import requests
import time
import sys
import random

from influxdb import InfluxDBClient


def test():

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')
    dbs = client.get_database_list()

    if 'test' not in [db['name'] for db in dbs]:
        client.create_database('test')


    for i in range(1000):
        start = time.time()
        #requests.get('http://blog.ziade.org/tools.html')
        time.sleep(float(random.randint(1, 1000))/1000.)
        duration = time.time() - start

        json_body = [{'points': [[str(i), duration, time.time()]],
                      'name': 'test',
                      'columns': ["request", "duration", "when"]}]

        client.write_points(json_body)
        time.sleep(.1)
        sys.stdout.write('.')
        sys.stdout.flush()


if __name__ == '__main__':
    test()
