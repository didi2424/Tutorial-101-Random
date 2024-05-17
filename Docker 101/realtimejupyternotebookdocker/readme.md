<h3 align="center">How to install Tensorflow on Docker With GPU Compatible Real Time Collaboration</h3>
<p align="center">
    <a href="" target="_blank">
        <img width="100%" src="/Docker 101/assets/BadgeDockerRealtimeJupyter.png" alt="Banner">
    </a>
</p>


<p align="center"> 
  This repository contains step how to build Tensorflow on Docker with GPU compitable with Jupyter hub and Jupyter Collaboration Remote to work Together. 
</p>

### ⚡️ Quick start
First, download and install Docker Desktop. Version 26.0.0 or higher is required.
```sh
Note! Enable/Check WSL 
```
Install Nvidia Driver 550.54.14 on Windows Host

enable WSL on Windows Machine

all link of Downloads or instruction in the Official Website [Official Website](#iii-official-website) or follow my instruction below to see the instruction [Installation](#i-installation-)

### Contents:
- [Categories](#categories)
    - [I. Installation 🚀](#i-installation-)
    - [II. Common Error That I found 📝](#ii-common-error-that-i-found-)
    - [III. Official Website](#iii-official-website)
- [Tools](#tools)
- [Articles](#articles)
- [Video Tutorials](#tutorials)
- [Contribute](#contribute)
- [Contact](#contact)

## Categories

#### I. Installation 🚀
1. Open PowerShell as Administrator
   ```sh
    wsl --install
   ```

2. Type your username dan password for WSL

3. Install Docker Desktop Configuration Check WSL2

4. Open VS Code and open Terminal in VS code
 
5. Make Share Folder (Because Ubuntu WSL is Virtual we need save our file into harddrive windows)

    ```sh
    sudo mkdir /mnt/project
    
    sudo mount -t drvfs '<Directory to mouth>' /mnt/project

    eg : sudo mount -t drvfs 'D:\Person\Data Dimas\17. Cloud WSL' /mnt/project
    ```

6. Change to Directory
    ```sh 
    cd /mnt/project
    ```
7. Make Dockerfile

    in Terminal WSL
    ```sh
    code Dockerfile
    ```
    Dockerfile
    ```sh
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
    ```


8. Jupyter Hub Config
    ```sh
    code jupyterhub_config.py
    ```
    jupyterhub_config.py
    ```sh
    c.Authenticator.allowed_users = {'user1', 'user2'}
    c.LocalAuthenticator.create_system_users = True
    c.Spawner.env.update({'LD_LIBRARY_PATH': '/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'})
    c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL', 'JUPYTERHUB_SINGLEUSER_APP','LD_LIBRARY_PATH']
    ```
9. Requirments.txt

    ```sh
    code requirments.txt
    ```
    requirments.txt
    ```sh
    jupyter
    notebook
    jupyterhub
    jupyter-collaboration
    tensorflow==2.16.1
    ```

9. Docker Compose YAML
    ```sh
    code docker-compose.yaml
    ```
    docker-compose.yaml
    ```sh
    version: '1.0'
    services:
        jupyter-hub:
        build: .
        ports:
            - '8000:8000'
        volumes:
            - ./dataset:/dataset
        deploy:
            resources:
                reservations:
                devices:
                    - driver: nvidia
                    count: 1
                    capabilities: [gpu]
    ```
10. Make Directory at '/mnt/project'
    ```sh
    sudo mkdir dataset
    ```


11. Build
```sh
docker-compose up
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### II. Common Error That I found 📝

##### 1. During docker-compose up Warning 'docker-compose' could not be found

dimas@DESKTOP-D8N0KT4:/mnt/project$ docker-compose up

The command 'docker-compose' could not be found in this WSL 2 distro.
We recommend to activate the WSL integration in Docker Desktop settings.

For details about using Docker Desktop with WSL 2, visit:

https://docs.docker.com/go/wsl2/

##### Step to fix
  run docker in wsl terminal
  ```sh
  docker
  ```





#### III. Official Website
https://www.docker.com/products/docker-desktop/
https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64
https://www.nvidia.com/download/index.aspx

https://learn.microsoft.com/en-us/windows/wsl/install
## Contact

## Buy Me a Coffe 🙇
* [![ETH][ETH]][ETH-url] BEP20 0x74d7ae669da2a05875f8036e3a3fefdf1f657e04

[🔼 Back to top](#How-to-install-Tensorflow-on-Docker-With-GPU-Compatible-Real-Time-Collaboration)


[ETH]: https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white
[ETH-url]: https://binance.com/
