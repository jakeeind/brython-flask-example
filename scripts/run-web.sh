#!/bin/sh

FLASK_ENV=development MYAPP_SETTINGS=$(pwd)/myApp.cfg DEBUG=1 myApp-web -d