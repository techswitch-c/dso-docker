# TechSwitch's Docker | DevSecOps

[Architecture Documentation](Documents/Architecture.md)
[Components](Documents/Components.md)


### Commands

- `docker --version`                                            # prints docker version
- `docker build .`                                             #  builds image from dockerfile
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
- `docker logs -f ubuntu-container`                                # print logs of the container
- `docker exec containerid /bin/bash`                                 #  shell of the container in interactive mode




 
> cd /usr/share/nginx/html 
>> sed -i  's/nginx/techswitch/g' index.html


Other Public registries

[Docker Hub](https://hub.docker.com/)

[Amazon ECR Public Gallery](https://gallery.ecr.aws/)

[How to publish images to AWS](https://docs.aws.amazon.com/AmazonECR/latest/public/public-getting-started.html)

[JFrog](https://jfrog.com/container-registry/)

[Working with Github Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#pushing-container-images)


