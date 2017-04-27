# Evangalion

A dockerized instrumentation sidecar. 


## Build and run in docker

```
docker build -t evangalion .
docker run -d -p 5000:5000 -v $CONFIG_FILE:/app/$CONFIG_FILE evangalion
```

