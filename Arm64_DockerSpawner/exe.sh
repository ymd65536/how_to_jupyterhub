# !bin/bash

# aarch64
uname -m

sudo amazon-linux-extras install docker=latest
sudo systemctl enable docker.service
sudo systemctl start docker.service

# 動作確認
docker version
docker ps

# docekrコマンドをsudoを付けずに実行できるようにするための設定です
sudo usermod -aG docker ec2-user
docker network create jupyterhub
docker build -t hub .
docker pull jupyter/base-notebook@sha256:28c8dd073626e407af4b79dc99ae74eccb283b09ccecedc8482226954c9449d1
docker run --rm -itd -v /var/run/docker.sock:/var/run/docker.sock --net jupyterhub --name jupyterhub -p 8000:8000 hub
