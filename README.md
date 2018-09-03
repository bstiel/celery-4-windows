## Create virtual env and install pip packages

```
C:\Developer\celery-4-windows>virtualenv celery-windows
C:\Developer\celery-4-windows>activate celery-windows
(celery-windows) C:\Developer>pip install -r requirements.txt
```

## Start Celery worker

Use any of the 3 commands to start the worker, explicitly *not* using the default prefork pool:

```
(celery-windows) C:\Developer\celery-4-windows>celery worker --app=app.app --pool=eventlet --loglevel=INFO
(celery-windows) C:\Developer\celery-4-windows>celery worker --app=app.app --pool=gevent --loglevel=INFO
(celery-windows) C:\Developer\celery-4-windows>celery worker --app=app.app --pool=solo --loglevel=INFO
```


## Execute Celery task asynchronously
In a new command prompt window:

```
C:\Developer>activate celery-windows
(celery-windows) C:\Developer\celery-4-windows>python app.py
```
