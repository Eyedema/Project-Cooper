## Project Cooper

Developing a simple application with Docker.

Run it with:
```
docker run -d --name <name> -p 5000:5000 -e ENVKEY=<yourvalue> --net <networkname> <imagename>:latest
```

Where:
* `name` is the name of the cointainer that will be created
* `yourvalue` is the value you want to give to the environment key
* `networkname` is the name of the network to which this container will connect. **WARNING**: your mysql container _must_ be connected to the same network
* `imagename` is the name of the image created with the provided Dockerfile 

Then connect to `localhost:5000` and verify that everything is working as expected.