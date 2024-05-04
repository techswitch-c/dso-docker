# TechSwitch's Docker | DevSecOps 💻
![alt text](docker-logo-blue.png)
## [Architecture Documentation](Documents/Architecture.md)
## [Components](Documents/Components.md)
## [Storage/others](Documents/Others.md)
### [PPT](Documents/Docker.pptx)
### [PDF](Documents/Docker-deepdive.pdf) 



### Important Commands 📋

- ` docker --version` # print docker version
- `docker build -t imagename:v1 .` # build image from dockerfile
- `docker build -t imagename:latest -f dockerfile_custome .` # create image from custom docker file
- `docker ps` # shows running containers
- `docker ps -a` # shows all containers, running/stopped/exited
- `docker stop containername` # stop container
- `docker stop $(docker ps -aq)` # stop all running containers at a time
- `docker search imagename` # searches image name in dockerhub
- `docker search f stars=100 f is official=true nginx` # search with filters
- `docker pull imagename`   # Pulls image from docker hub​
- `docker run​ imagename`                                       #  downloads and runs container
- `docker login -u username --password-stdin`                 #   login to docker hub from cli
- `docker images`                                            #  lists images
- `docker ps -a`                                              #  list containers
- `docker tag imagename:tag username/image:tag`               #  add tag to image before pushing to registry
- `docker push imagename username/image:tag`                    # push image to docker hub
- `docker push ghcr.io/phanatic/app:1.0.0`                       #  pushing image to github container registry
- `docker rmi containername`                                     #  removes docker container
- `docker container run -d --name mynginx -p 8080:80 nginx`         # expose an nginx container with 8080 port
- `docker container inspect containername`                         # check the full details of a container
- `docker logs -f ubuntu-container`                                # print logs of the container
- `docker exec containerid /bin/bash`                                 #  shell of the container in interactive mode
- `docker run -d --name httpd  --mount source=test1,target=/tmp/fs httpd` # bind mount using --mount flag
- `docker run -d --name nginx2 -v test1:/tmp2/fs nginx`   # attach volume using -v/--volume flag
- `docker run -d --name nginx3 -v /local/dir:/tmp nginx` # attach local directory to container
- `docker info`                   # shows information of everything, look out for storage drivers, network types
- `docker volume inspect test1` # check informatin about specific volume
- `docker volume rm test1` # remove volume from the list
- `docker volume prune` # removes all unused volumes
- `docker network ls` # list down the networks
- `docker run --rm -d --network host --name nginx3 nginx`   # attach to host network & access through localhost
- `docker network create custom` # creates a custom network other than default
- `docker network disconnect containername` # disconnect docker container from attached network
- `docker network inspect bridge` # check the details of a network
- `docker network connect bridge containername`   # connect network to particular network type/driver
- `docker network prune` # deletes all unused network types
- `docker run --name nginx5 -d -p 8082:80 nginx` # publish port destination:source
- `docker network rm custom` # removes custom network from the list
- `brctl show` # bridge cli util to show the details for bridge network
- `docker image export containername > container.tar`  # create a tarball of container fs
- `docker image import` # create an image from a tarball
- `docker image history` # shows the image building history
- `docker image save` # backup of image
- `docker image load` # restore images and tags from tar
- `DOCKER_BUILDKIT=1 docker build --no-cache -f dockerfile_multi --target step2 .`  # run specific stage in multi-stage

---
**NOTE**
Add `CMD ["sh", "-c", "sleep infinity"]` to the dockerfile to keep container running
---
## Docker-Compose

Install and use docker-compose standalone

> sudo curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
> sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
> chmod a+x /usr/local/bin/docker-compose

 
`docker-compose -h`

### CLI CheatSheet

[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff)](https://docs.docker.com/reference/cli/docker/)


 
>>docker exec -it nginx /bin/bash -- sed -i  's/nginx/techswitch/g' /usr/share/nginx/html/index.html


Other Public registries 🫙

[Docker Hub](https://hub.docker.com/)

[Amazon ECR Public Gallery](https://gallery.ecr.aws/)

[How to publish images to AWS](https://docs.aws.amazon.com/AmazonECR/latest/public/public-getting-started.html)

[JFrog](https://jfrog.com/container-registry/)

[Working with Github Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#pushing-container-images)


