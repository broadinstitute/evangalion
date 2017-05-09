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

## Notes

Mock compose with eva and statsd, using local ui:
```yaml
ui:
  image: broadinstitute/firecloud-ui:dev
  ports:
    - "80:80"
    - "443:443"
    - "8000:8000"
  volumes:
    - ./ca-bundle.crt:/etc/ssl/certs/ca-bundle.crt
    - ./server.crt:/etc/ssl/certs/server.crt
    - ./server.key:/etc/ssl/private/server.key
    - .:/config:rw
  environment:
    SERVER_NAME: local.broadinstitute.org
    HTTPS_ONLY: "false"

statsd:
    image: visity/statsd
    ports:
      - "8125:8125/udp"
    volumes:
      - ./statsdConfig.js:/opt/statsd/config.js

evangalion:
  image: evangalion
  ports:
    - "5000:5000"
  links:
    - ui:ui
    - statsd:statsd
  volumes:
    - ./config.yml:/app/config.yml:ro
  command: app.py ./config.yml
  environment:
    - PYTHONUNBUFFERED=0
```