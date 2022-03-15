workers = 4
worker_class = 'gevent'
worker_connections = 128
pidfile = 'gunicorn.pid'

daemon = True
bind = '0.0.0.0:80'

accesslog = 'access.log'
errorlog = 'error.log'