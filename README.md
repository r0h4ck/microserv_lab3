### Flask microservice with Hazelcast

#### structure:
* facade-service: main access point of system
  * app.py: main API off system
  * Dockerfile: container for facade-service
* logging-service: service that stores messages in memory
  * app.py: logger API
  * Dockerfile: container for logging-service
* messages-service: empty service
  * app.py: empty API
  * Dockerfile: container for messages-service
* docker-compose.yml: start point
* main.py: testing script

**docker-compose.yml usage:**
```shell
$ sudo docker-compose up
```
to rebuild container
```shell
$  sudo docker-compose up --no-deps --build 
```
**To use project:**
```shell
$ python3 runner.py -m 'METHOD' -t = 'text message' -n = "number to send count" 
```
**example of use [POST]:**
```shell
$ python3 main.py -m post -t "test message" -n 10
```
**example of use [GET]:**
```shell
$ python3 main.py -m get
```
