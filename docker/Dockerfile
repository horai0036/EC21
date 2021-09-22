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

#RUN apt install -y python3-pip
#RUN python3 -m pip install --upgrade pip

WORKDIR /home/kojima/sfm_flow2021
#RUN conda update --all
ADD requirements.txt /home/kojima/sfm_flow2021
RUN pip install -r requirements.txt
#RUN conda install -c conda-forge argparse
#RUN conda install -c conda-forge tensorboardx
#RUN conda install -c conda-forge blessings
#RUN conda install -c conda-forge progressbar2
#RUN conda install -c conda-forge tqdm
#RUN conda install -c conda-forge pebble

# move to root directory
WORKDIR /home/kojima
#RUN pip3 install torch torchvision

