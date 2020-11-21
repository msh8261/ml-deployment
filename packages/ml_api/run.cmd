#!/usr/bin/env bash
set IS_DEBUG=${DEBUG:-true}
exec gunicorn --bind 0.0.0.0:5000 - run:app