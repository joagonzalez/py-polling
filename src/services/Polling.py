import sys
sys.path.append('../')
import requests
import time
import json
from influxdb import InfluxDBClient
from services.loggerService import loggerService
from config.settings import config
from services.Service import Service


class Polling:
    def __init__(self):
        self.influxdb_host = config['INFLUX']['HOST']
        self.influxdb_port = config['INFLUX']['PORT']
        self.influxdb_ssl = config['INFLUX']['SSL']
        self.influxdb_verify_ssl = config['INFLUX']['VERIFY_SSL']
        self.influxdb_database = config['INFLUX']['DATABASE']
        self.influxdb_measurement = config['INFLUX']['MEASUREMENT']
        self.services = []
        self.load_services()
    
    def __str__(self):
        return 'Polling class. Conector: {}:{} - Database: {} - Measurement: {}'.format(
            self.influxdb_host, self.influxdb_port, self.influxdb_database, self.influxdb_measurement
        )

    def load_services(self):
        """
        Load built urls to poll
        """
        for service, values in config['SERVICES'].items():
            s = Service(service, values['URL'], values['PORT'], values['ENDPOINT'])
            self.services.append(s.get_service())

    def parse_data_influxdb(self, data):
        """
        Adapt status information for influxdb api
        """
        parsed = []
        data_time = int(time.time() * 1000) #milliseconds

        for services in data:
            for service, values in services.items():
                loggerService.info(service)
                s = {}
                s['tags'] = {}
                s['fields'] = {}
                s['measurement'] = config['INFLUX']['MEASUREMENT']
                s['time'] = data_time
                s['tags']['service'] = str(service)
                s['fields']['metric_1'] = float(values['metric_1'])
                s['fields']['metric_2'] = float(values['metric_2'])
                s['fields']['status'] = str(values['status'])

                loggerService.info(service)
                loggerService.info(values)
                parsed.append(s)
        loggerService.info('influxDB object: ' + json.dumps(parsed, indent=4))
        return parsed

    def write_influxdb(self, data):
        """
        Write parsed status results from a specific service to influxdb
        """
        try:
            client = InfluxDBClient(host=self.influxdb_host, port=self.influxdb_port, 
                                    ssl=self.influxdb_ssl, verify_ssl=self.influxdb_verify_ssl,
                                    database=self.influxdb_database)
            client.create_database(self.influxdb_database)
            client.write_points(data, protocol='json', time_precision='ms')
        except Exception as e:
            loggerService.error('Error writing points into influxDB')
            loggerService.error('Error: ' + str(e))

    def polling(self):
        """
        Poll status endpoint of every service loaded in settings.py
        """
        results = []
        try:
            for service in self.services:
                r = requests.get(list(service.values())[0])
                results.append(
                        {list(service.keys())[0]: r.json()}
                    )
            loggerService.info('results: ' + str(results))
            loggerService.info('data parsed: ' + str(self.parse_data_influxdb(results)))
            data_parsed = self.parse_data_influxdb(results)
            self.write_influxdb(data_parsed)
        except Exception as e:
            loggerService.error('Error polling service status API: ' + str(service))
            loggerService.error('Error: ' + str(e))
    
    def get_services(self):
        """
        Return services to be monitored within newcos
        """
        return self.services

if __name__ == '__main__':
    polling = Polling()
    loggerService.info(polling)
    loggerService.info(polling.get_services())
    polling.polling()

