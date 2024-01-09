# Celery (but better use Redpanda :D )
 
Task queues are used as a mechanism to distribute work across threads or machines.

A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform.

[Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.

Add the below code to `docker-compose.yml` to enable Celery module:

```
  redis:
    image: "redis:alpine"
    container_name: redis-db

  celery-worker:
    restart: unless-stopped
    build:
      context: heal-diapp
    command: celery -A main worker -l info
    depends_on:
      - web
      - redis
    # container_name: celery-worker

  celery-beat:
    restart: unless-stopped
    build:
      context: heal-diapp
    # command: celery -A main beat -l info
    depends_on:
      - web
      - redis
    container_name: celery-beat
    
```