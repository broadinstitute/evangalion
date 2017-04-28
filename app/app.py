import sys, os
from entryPlug import EntryPlug
from flask import Flask, request
import importlib
import json

app = Flask(__name__)
plug = EntryPlug(sys.argv[1])


## Routes ##

@app.route('/')
def hello_world():
    return 'Evangalion Appliction, Dockerized'

@app.route('/check', methods=['GET'])
def health_check():
    print request
    health_map = {}
    for check in plug.checkers:
        health_map[check] = call_plugin(check, "checks")

    unhealthy = find_unhealthy(health_map)
    if unhealthy:
        return json.dumps(unhealthy), 500
    else:
        return "Everything healthy!", 200

## Plugin methods ##

def call_plugin(name, module, *args, **kwargs):
    plugin = importlib.import_module('.'.join((module, name)))
    try:
        return plugin.main(*args, **kwargs)
    except StandardError:
        print("module not found!")


## Health check methods ##
# probably want to move these to own namespace

# takes a map check -> (bool, msg), filters by things that have come up with their health as False
def find_unhealthy(checks):
    return {k:v for k,v in checks.iteritems() if v[0] == False }


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    app.config.from_envvar('APP_HOST')
    print app.config.get('APP_HOST')