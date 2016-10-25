# flask-nginx-starter
 A starter repo for a flask + nginx Docker container

## Step 1
- If you want to use this repo as a jumping off point for your repo, duplicate it. (If you forking it, it remains public.) To publicate it, clone the repository, update the git remote, and then push it up as a new repository under the new organization. There are more details [here](https://help.github.com/articles/duplicating-a-repository/)

- If you want to deploy this as an example, and pull the relevant parts into your own flask app, copy the [`Dockerfile`](https://github.com/opsolutely/flask-nginx-starter/blob/master/Dockerfile), [`nginx.conf`](https://github.com/opsolutely/flask-nginx-starter/blob/master/nginx.conf), [`run_local.sh`](https://github.com/opsolutely/flask-nginx-starter/blob/master/run_local.sh), and the [`docker_files` directory](https://github.com/opsolutely/flask-nginx-starter/tree/master/docker_files) into the root of your repository. 

- If you're only demoing, then the easiest thing is to deploy this repository as-is, without duplicating or pulling the configuration into your own repository.

## Step 2
In Opsolutely, select the repository to deploy, and when the you specify the dockerfile location, set up two Volumes:
Make the contents of `opsolutely/flask-nginx-starter/docker_files/supervisord.conf` available in the container at `/opt/code/`, and make `opsolutely/flask-nginx-starter/docker_files/service.conf` also available at `/opt/code/`. (You could alternatively add this in the dockerfile directly, but this is a nice way to try out the UI.)

## Step 3
Answer a few painless questions, and click deploy! :rocket:



