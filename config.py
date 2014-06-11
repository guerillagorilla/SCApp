#!/usr/bin/python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

ADMINS = frozenset(['jason.jugar@sprint.com'])
SECRET_KEY = os.environ['FLASK_SECRET_KEY']

DATABASE = 'testdb'

#CSRF_ENABLED = True
#CSRF_SESSION_KEY = os.environ['FLASK_SECRET_KEY']
