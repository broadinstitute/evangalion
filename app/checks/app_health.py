import requests

# All plugins should have a main method that returns a tuple of (healthy (bool), message)
def main(*args, **kwargs):
    #r = requests.get()
    print args[0]
    r = requests.get(args[0])
    print r.content
    healthy = False
    message = "App is healthy" if healthy else "App is unhealthy"
    return healthy, message
