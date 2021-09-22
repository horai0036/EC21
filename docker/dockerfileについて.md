# Dockerfileとは
Dockerのイメージを自動的に作成するファイル  
プログラムのように上から順に実行されていく  

内容はpipやaptコマンドなどをまとめたものが多い

# テンプレート  コマンドについて
* FROM [ベースとなるイメージ]  
から1行目が始まる．ベースとなるイメージの上にインストールしたいソフトウェアのインストールコマンドを書く  
ベースをCUDA,cuDNNにすると，CUDA,cuDNNのバージョンだけ決まるので研究室で従来行っているようにパッケージを入れることができる．  

* RUN [コマンド]  
を使うことで各Linux命令を記述できる．  
(例) RUN apt-get update  

* ENV  
環境変数．Pathを通したい時とかに使う．

# 以下CUDA10.0,cuDNN7.5,Ubuntu16.04にanacondaとpytorchをインストールした時の例
```
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

# update packages
RUN set -x && \
    apt-get update && \
    apt-get upgrade -y

# install command
RUN set -x && \
    apt-get install -y wget && \
    apt-get install -y sudo

# anaconda
RUN set -x
RUN wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
RUN bash Anaconda3-2019.10-Linux-x86_64.sh -b
RUN rm Anaconda3-2019.10-Linux-x86_64.sh

# path setteing
ENV PATH $PATH:/root/anaconda3/bin

RUN conda install pytorch==1.0.1 torchvision==0.2.2 cudatoolkit=10.0 -c pytorch
```
