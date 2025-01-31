[![Docker Pulls](https://badgen.net/docker/pulls/d3fk/s3cmd?icon=docker&label=pulls)](https://hub.docker.com/r/d3fk/s3cmd/tags) [![Docker Image Size](https://badgen.net/docker/size/d3fk/s3cmd/latest?icon=docker&label=image%20size)](https://hub.docker.com/r/d3fk/s3cmd/tags) [![Docker build](https://img.shields.io/docker/cloud/automated/d3fk/s3cmd?label=build&logo=docker)](https://hub.docker.com/r/d3fk/s3cmd/tags) [![Build status](https://img.shields.io/docker/cloud/build/d3fk/s3cmd?label=build%20status&logo=docker)](https://hub.docker.com/r/d3fk/s3cmd/tags) [![Docker Stars](https://badgen.net/docker/stars/d3fk/s3cmd?icon=docker&label=stars)](https://hub.docker.com/r/d3fk/s3cmd) [![Github Stars](https://badgen.net/github/stars/Angatar/s3cmd?icon=github&color=green)](https://github.com/Angatar/s3cmd) [![Github forks](https://badgen.net/github/forks/Angatar/s3cmd?icon=github)](https://github.com/Angatar/s3cmd/fork) [![Github open issues](https://badgen.net/github/open-issues/Angatar/s3cmd?icon=github)](https://github.com/Angatar/s3cmd/issues) [![Github closed issues](https://badgen.net/github/closed-issues/Angatar/s3cmd?icon=github)](https://github.com/Angatar/s3cmd/issues?q=is%3Aissue+is%3Aclosed) [![GitHub license](https://img.shields.io/github/license/Angatar/s3cmd)](https://github.com/Angatar/s3cmd/blob/master/LICENSE)

# s3cmd (Angatar> d3fk/s3cmd)
A simple s3cmd S3 client installed on the Alpine:latest container

Useful with any S3 compatible object storage system.

## Docker image

pre-build from Docker hub with "automated build" option.

image name **d3fk/s3cmd**

`docker pull d3fk/s3cmd`

Docker hub repository: https://hub.docker.com/r/d3fk/s3cmd/

[![DockerHub Badge](https://dockeri.co/image/d3fk/s3cmd)](https://hub.docker.com/r/d3fk/s3cmd)


### Image tag d3fk/s3cmd:latest

The **d3fk/s3cmd:latest** image available from the Docker Hub is built automatically (automated build on each change of this [image code repository](https://github.com/Angatar/s3cmd) + automated build triggered once per week) so that using the d3fk/s3cmd:latest image ensures you to have the latest updated(including security fixes) and functional version available of s3cmd in a lightweight alpine image.

### Image tag d3fk/s3cmd:stable
In case you'd prefer a fixed version of this d3fk/s3cmd container to avoid any possible change in its behaviour, the d3fk/s3cmd:stable image is also made available from the Docker hub. It contains the s3cmd S3 client version 2.2.0 in an Alpine Linux v3.14. This image had a stable behaviour observed in production, so that it was freezed in a release of the code repo and built from the Docker hub by automated build. It won't be changed or rebuilt in the future (the code is available from the "releases" section of this [image code repository on GitHub](https://github.com/Angatar/s3cmd)).

image:tag **d3fk/s3cmd:stable**
```sh
$ docker pull d3fk/s3cmd:stable
```


## Basic usage

```sh
docker run --rm -v $(pwd):/s3 -v $HOME/.s3:/root d3fk/s3cmd sync . s3://bucket-name
```
The first volume is using your current directory as workdir and the second volume is used for the configuration of your S3 connection.

## s3cmd settings

It basically uses the .s3cfg configuration file. If you are already using s3cmd locally the previous docker command will use the .s3cfg file you already have at ``$HOME/.s3/.s3cfg``. In case you are not using s3cmd locally or don't want to use your local .s3cfg settings, you can use the s3cmd client to help you to generate your .s3cfg config file by using the following command.

```sh
mkdir .s3
docker run --rm -ti -v $(pwd):/s3 -v $(pwd)/.s3:/root d3fk/s3cmd --configure
```
A blank .s3cfg file is also provided as a template in the [.s3 directory of the source repository](https://github.com/Angatar/s3cmd/tree/master/.s3), if you wish to configure it by yourself from scratch.

### s3cmd and encryption
s3cmd enables you with encryption during transfert with SSL if defined in the config file or if the option in metionned in the command line.
s3cmd also enables you with encryption at REST with server-side encryption by using the flag --server-side-encryption (e.g: you can specify the KMS key to use on the server), or client side encryption by using the flag -e or --encrypt. These options can also be defined in the .s3cfg config file.

### s3cmd complete documentation

See [here](http://s3tools.org/usage) for the documentation.


## Automatic Periodic Backups with Kubernetes

This container was created to be used within a K8s CRONJOB.
You can use the provided YAML file named s3-backup-cronjob.yaml as a template for your CRONJOB.
A configmap can easily be created from the .s3cfg config file with the following kubectl command:
```sh
kubectl create configmap s3config --from-file $HOME/.s3
```
Then, once configured with your data volume/path and your bucket (by completing the file or defining the ENV variables: YOUR_KMS_KEY_ID, YOUR_BUCKET_NAME, NFS_SERVER, SHARED-FOLDER), the k8s CRONJOB can be created from the file:
```sh
kubectl create -f s3-backup-cronjob.yaml
```
*Nb: the option for sync `--no-check-md5` speeds up the sync process since only size will be compared but it may also miss some changed files. However this option is usefull with server side encryption since the md5 signature of the encrypted files in the bucket will be different from the non-encrypted files that you need to back up.*

### s3cmd & mysql backups

In case you are interested in storing your database dumps into a S3 compatible object storage you'd probably prefer to use [d3fk/mysql-s3-backup](https://hub.docker.com/r/d3fk/mysql-s3-backup) also based on Alpine distrib and containing a mysql client in addition to the s3cmd tool.

[![GitHub license](https://img.shields.io/github/license/Angatar/s3cmd)](https://github.com/Angatar/s3cmd/blob/master/LICENSE)
