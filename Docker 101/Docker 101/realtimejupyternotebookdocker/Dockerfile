#Tensorflow 2.16.1 only works with cuda 12.2.2 Cudnn 8 At Mei 2024
FROM nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04

# In the Ubuntu 22.04 images, cudnn is placed in system paths. Move them to
# /usr/local/cuda
RUN cp -P /usr/include/cudnn*.h /usr/local/cuda/include
RUN cp -P /usr/lib/x86_64-linux-gnu/libcudnn* /usr/local/cuda/lib64
ENV LD_LIBRARY_PATH="/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
RUN echo $LD_LIBRARY_PATH

ARG DEBIAN_FRONTEND=noninteractive

# install scripts.
RUN apt-get update \
    && apt-get install -y python3-pip \
    && apt-get install -y npm \
    && apt-get install -y sudo \
    && npm install -g configurable-http-proxy

# Install all Requirments
COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt

# Add user to login in Jupyter Hub
RUN useradd -m user1 && \
    useradd -m user2 && \
    echo 'user1:00000000' | chpasswd && \
    echo 'user2:00000000' | chpasswd

# Grant sudo privileges to user1
RUN usermod -aG sudo user

# Install JupyterHub and Jupyter Notebook
COPY jupyterhub_config.py /etc/jupyterhub/
EXPOSE 8000

# Set the command to start JupyterHub
CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]