# Evangalion

A dockerized instrumentation sidecar. 


## Build and run in docker

```
docker build -t evangalion .
docker run -d -p 5000:5000 -v $CONFIG_FILE:/app/$CONFIG_FILE evangalion
```

## Use Case

Run in tandem with docker-compose that runs one or more containers to monitor.

Load configuration yaml file as volume, in it include
* checks - name of health check modules to run
* environment variables needed for checkers such as APP_HOST, etc

Load any additional check modules into `/app/checks`.  Should be written in python.
These plugins should all have a `main` method that 
* takes `(*args, **kwargs)` as parameters
* returns a tuple of `(healthy? {bool}, message {str})`
