import sys, os
from entryPlug import EntryPlug
from flask import Flask
import importlib

app = Flask(__name__)
plug = EntryPlug(sys.argv[1])


## Routes ##

@app.route('/')
def hello_world():
    return 'Evangalion Appliction, Dockerized'

@app.route('/check')
def health_check():
    health_map = {}
    for check in plug.checkers:
        health_map[check] = call_plugin(check, "checks")

    unhealthy = find_unhealthy(health_map)
    if unhealthy:
        return "Something was unhealthy", 500
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


def formulate_health_response(unhealthy):
    pass


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    # TODO: load in a bunch of configuration stuff from service we are attached to