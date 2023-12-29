# Asynchronous API with FastAPI and Pytest

## Build the image and run the container:

```sh
$ docker-compose up -d --build
```

## Update the image and run unit test:

```sh
$ docker-compose exec web pytest .
```

Test out the following routes:

1. [http://localhost:8002/status_check](http://localhost:8002/status_check)
1. [http://localhost:8002/docs](http://localhost:8002/docs)
1. [http://localhost:8002/notes](http://localhost:8002/notes)

