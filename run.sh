#!/bin/sh

WORKERS=${WEB_CONCURRENCY:-3}
TIMEOUT=${GUNICORN_TIMEOUT:-120}
WORKER_CLASS=${GUNICORN_WORKER_CLASS:-sync}

echo "Starting app with $WORKERS workers..."

exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers $WORKERS \
    --timeout $TIMEOUT \
    --worker-class $WORKER_CLASS
