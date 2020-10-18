#!/bin/bash
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Please activate your python enviroment before setup"
    exit 1
else
    echo $VIRTUAL_ENV
    echo "VIRTUAL_ENV is set"
fi

echo 'Setup the development project'
sleep 1

python3 setup.py develop

python3 setup.py develop
