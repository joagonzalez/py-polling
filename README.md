# newcos-polling
# Infrastructure as Code
![Python](https://img.shields.io/badge/pypolling-v1.0.0-orange)
![Python](https://img.shields.io/badge/schedule-0.6.0-blue)
![Python](https://img.shields.io/badge/Flask-v1.1.2-blue)
![Python](https://img.shields.io/badge/pymsteams-0.1.13-blue)
![Python](https://img.shields.io/badge/platform-linux--64%7Cwin--64-lightgrey)

This python service extract information from different services loaded in *src/config/settgins.py*, parse that information and then writes it into influxDB in orther to build dashboard that allow to monitor in real-time.

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

## Mock server

### Build
```
docker-compose build
```

### Run
```
docker-compose up
```