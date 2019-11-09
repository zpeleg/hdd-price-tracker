#!/usr/bin/env bash
service nginx start
uwsgi --ini web/uwsgi.ini
