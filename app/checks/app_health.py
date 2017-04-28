import requests

# All plugins should have a main method that returns a tuple of (healthy (bool), message)
def main():
    healthy = False
    message = "App is healthy" if healthy else "App is unhealthy"
    return healthy, message
