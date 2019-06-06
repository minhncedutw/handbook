
## 10 CLI commands
1. Lists running containers: `docker ps`

2. Download a image: `docker pull`

3. Builds Docker images from a Dockerfile: `docker build -t my_container .`

4. Run a docker container based on an image: `docker run my_image -it bash`

5. Display the logs of a container: `docker logs --follow my_container`

6. This lists the volumes: `docker volume ls`

7. Removes one or more containers: `docker rm my_container`

8. Removes one or more images: `docker rmi my_image`

9. Stops one or more containers: `docker stop my_container` or `docker kill my_container`

10. Use them together:
 - kill all running containers: `docker kill $(docker ps -q)`
 - delete all stopped containers: `docker rm $(docker ps -a -q)`
 - delete all images: `docker rmi $(docker images -q)`