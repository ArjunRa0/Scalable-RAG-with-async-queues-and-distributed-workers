from rq import Queue

queue = Queue(connection=Redis(
host='localhost', port=6379
))