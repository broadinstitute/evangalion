import requests

# Given a host, returns a 
def simple_health_check(host):
    if not host:
        raise StandardError("Error! APP_HOST not set.")

    health_endpoint = host + "/health"
    r = requests.get(health_endpoint)
    health = True if r.status_code == 200 else False
    message = "App is healthy" if health else "{0} returned {1}".format(health_endpoint, r.status_code)
    return health, message


# All plugins should have a main method that returns a tuple of (health (bool), message)
def main(**kwargs):
    return simple_health_check(kwargs.get('APP_HOST'))
