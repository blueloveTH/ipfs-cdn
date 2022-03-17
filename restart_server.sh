#!/bin/sh

kill -9 $(cat gunicorn.pid)
sleep 1
gunicorn app:app -c gunicorn.py