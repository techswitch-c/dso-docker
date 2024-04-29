# TechSwitch's Docker | DevSecOps

## [Architecture Documentation](Documents/Architecture.md)
## [Components](Documents/Components.md)


### Commands

## print docker version
```
docker --version
```

##  build image from dockerfile
```
docker build -t name .
```

- `docker ps` # shows running containers
- `docker ps -a` # shows all containers, running/stopped/exited
- `docker stop containername` # stop container
- `docker stop $(docker ps -aq)` # stop all running containers at a time
- `docker pull imagename`   # Pulls image from docker hub​
- `docker run​ imagename`                                           #  downloads and runs container
- `docker login -u username --password-stdin`                                            #   login to docker hub from cli
- `docker images`                                            #  lists images
- `docker ps -a`                                              #      list containers
- `docker tag imagename`                                            #  add tag to image
- `docker push imagename username/image:tag`                                            # push image to docker hub
- `docker push ghcr.io/phanatic/app:1.0.0`                       #  pushing image to github container registry
- `docker rmi containername`                                            #  removes docker container
- `docker container run -d --name mynginx -p 8080:80 nginx`         # expose an nginx container with 8080 port
- `docker container inspect containername`                         # check the full details of a container
- `docker logs -f ubuntu-container`                                # print logs of the container
- `docker exec containerid /bin/bash`                                 #  shell of the container in interactive mode
- `docker run -d --name httpd  --mount source=test1,target=/tmp/fs httpd` # bind mount using --mount flag
- `docker run -d --name nginx2 -v test1:/tmp2/fs nginx`   # attach volume using -v/--volume flag
- `docker run -d --name nginx3 -v /local/dir:/tmp nginx` # attach local directory to container, source to destination
- `docker info`                     # shows information of everything, look out for storage drivers, network types
- `docker volume inspect test1` # check informatin about specific volume
- `docker volume rm test1` # remove volume from the list
- `docker volume prune` # removes all unused volumes
- `docker network ls` # list down the networks
- `docker run --rm -d --network host --name nginx3 nginx`   # attach nginx container to host network and access directly through localhost
- `docker network create custom` # creates a custom network other than default
- `docker network disconnect containername` # disconnect docker container from attached network
- `docker network inspect bridge` # check the details of a network
- `docker network connect bridge containername`   # connect network to particular network type/driver
- `docker network prune` # deletes all unused network types
- `docker run --name nginx5 -d -p 8082:80 nginx` # publish port for any container with -p flag on default network
- `docker network rm custom` # removes custom network from the list
- `brctl show` # bridge cli util to show the details for bridge network






 
>>docker exec -it nginx /bin/bash -- sed -i  's/nginx/techswitch/g' /usr/share/nginx/html/index.html


Other Public registries

[Docker Hub](https://hub.docker.com/)

[Amazon ECR Public Gallery](https://gallery.ecr.aws/)

[How to publish images to AWS](https://docs.aws.amazon.com/AmazonECR/latest/public/public-getting-started.html)

[JFrog](https://jfrog.com/container-registry/)

[Working with Github Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#pushing-container-images)


