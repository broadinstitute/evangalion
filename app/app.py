import sys, os
from entryPlug import EntryPlug
from flask import Flask, request
import importlib
import json
import statsd

## Initialize ##

app = Flask(__name__)
plug = EntryPlug(sys.argv[1])
app_name = plug.environment.get('APP')
stats_client = statsd.StatsClient("statsd", 8125, prefix=app_name)

## Routes ##

@app.route('/')
def hello_world():
    return 'Evangalion Appliction, Dockerized'

@app.route('/check', methods=['GET'])
def health_check():
    health_map = {}

    for check in plug.checkers:
        health_map[check] = call_plugin(check, "checks", **plug.environment)

    unhealthy = find_unhealthy(health_map)
    if unhealthy:
        stats_client.incr('health_check.500')
        return json.dumps(unhealthy), 500
    else:
        stats_client.incr('health_check.200')
        return "Everything healthy!", 200

## Plugin methods ##

def call_plugin(name, module, **kwargs):
    plugin_name = '.'.join((module, name))
    plugin = importlib.import_module(plugin_name)
    return plugin.main(**kwargs)


## Health check methods ##
# probably want to move these to own namespace

# takes a map check -> (bool, msg), filters by things that have come up with their health as False
def find_unhealthy(checks):
    return {k:v for k,v in checks.iteritems() if v[0] == False }


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')