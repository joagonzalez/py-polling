# py-polling
![Python](https://img.shields.io/badge/pypolling-v1.0.0-orange)
![Python](https://img.shields.io/badge/schedule-0.6.0-blue)
![Python](https://img.shields.io/badge/Flask-v1.1.2-blue)
![Python](https://img.shields.io/badge/pymsteams-0.1.13-blue)
![Python](https://img.shields.io/badge/platform-linux--64%7Cwin--64-lightgrey)

This python service extract information from different services loaded in *src/config/settings.py*, parse that information and then writes it into influxDB in order to build dashboards that allow monitoring in real-time.

In order to test the service, a docker-compose file was created with a mock-server using Flask in which random data is collected and then loaded in another influxDB service.


**Content**
- [Getting started](#getting-started)
- [Polling](#polling)
- [Mock server](#mock-server)
- [Build](#docker)
- [Run](#run)
- [References](#references)


## Getting started

Dir structure of repo
```
├── dashboard
├── mock-server
└── src
    ├── config
    ├── logs
    ├── services
    └── utilities

7 directories
```

## Polling
APIs polling service using schedule library. The app loop will trigger pending scheduled tasks every 1 second.

```python
def main():
    """
    Executes main application and schedule task
    """
    loggerService.info('Loading scheduled tasks...')
    schedule.every(config['SCHEDULER']).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
```

## Mock server
Flask based mock server to test polling information from different endpoints.

### Build
```
docker-compose build 
```

### Run
```
docker-compose up
```
