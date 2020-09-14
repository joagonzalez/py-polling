config = {
    'BUILDING': {
        'VERSION': '1.0.2',
        'PROJECT': 'py-polling',
        'DOCKER_REGISTRY': 'dockerhub.com',
        'NAME': 'polling'
    },
    'SERVICES': {
        'serviceA': {
            'URL': 'http://mock-api',
            'PORT': '5000',
            'ENDPOINT': '/serviceA/status'
        },
        'serviceB': {
            'URL': 'http://mock-api',
            'PORT': '5000',
            'ENDPOINT': '/serviceB/status'
        }
    },
    'INFLUX': {
        'HOST': 'influxdb',
        'PORT': 8086,
        'SSL': False,
        'VERIFY_SSL': False,
        'DATABASE': 'polling',
        'MEASUREMENT': 'services'
    },
    'LOGGER': 'app_debug',
    'SCHEDULER': 0.1,
    'WEBHOOK': 'https://outlook.office.com/webhook/327044bc-8860-4705-a521-48cc9bfd264e@58005ddb-3d82-4718-9e75-ec5c71cca7ec/IncomingWebhook/ce255d45adfd4d94aa803a84e86e1d6f/4b94f775-45ba-4f8d-a767-252cb12f9726'
}