import schedule
import time
from services.loggerService import loggerService
from config.settings import config
from services.Polling import Polling
# agregar argparse

#!/usr/bin/env python3
"""
Script for /status endpoint polling within newcos-platform services
"""
def script_time(start, end):
    return end - start

def job():
    """
    Job that execute task to be scheduled
    """
    polling = Polling()
    loggerService.info(polling)
    loggerService.info(polling.get_services())

    start = time.time()
    polling.polling()
    end = time.time()
    loggerService.info('Time execution: ' + str(script_time(start, end)))    


def main():
    """
    Executes main application and schedule task
    """
    loggerService.info('Loading scheduled tasks...')
    schedule.every(config['SCHEDULER']).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
