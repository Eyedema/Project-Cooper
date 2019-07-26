## Project Cooper

Developing a simple application with Docker.

Run it with:
```
docker run -d --name <name> -p 5000:5000 -e ENVKEY=<yourvalue> --net <networkname> <imagename>:latest
```

Where:
* `name` is the name of the cointainer that will be created
* `yourvalue` is the value you want to give to the environment key
* `networkname` is the name of the network to which this container will connect.
...*WARNING*: it _must_ be the same netowork to which you mysql container is connected.
* `imagename` is the name of your image created with the provided Dockerfile 