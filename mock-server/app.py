from flask import Flask
import json
import random

app = Flask(__name__)

@app.route('/serviceA/status')
def serviceA():
    serviceA_data = {
        'metric_1': str(random.randint(0,100)),
        'metric_2': str(random.randint(0,100)),
        'status': 'online' 
    }

    return json.dumps(serviceA_data)

@app.route('/serviceB/status')
def serviceB():
    serviceB_data = {
    'metric_1': str(random.randint(0,100)),
    'metric_2': str(random.randint(0,100)),
    'status': 'offline' 
    }

    return json.dumps(serviceB_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)