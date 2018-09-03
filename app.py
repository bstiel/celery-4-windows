import os
import logging
from celery import Celery


logger = logging.getLogger(__name__)

app = Celery('app')
app.conf.update({
    'broker_url': 'filesystem://',
    'broker_transport_options': {
        'data_folder_in': './broker/out',
        'data_folder_out': './broker/out',
        'data_folder_processed': './broker/processed'
    }})


# setup folder for message broking
for f in ['./broker/out', './broker/processed']:
    if not os.path.exists(f):
        os.makedirs(f)


@app.task()
def add(x, y):
    result = x + y
    logger.info(f'Add: {x} + {y} = {result}')
    return result


if __name__ == '__main__':
    task = add.s(x=2, y=3).delay()
    print(f'Started task: {task}')