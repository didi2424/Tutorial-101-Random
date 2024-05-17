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
    - [II. Usage 🧪](#ii-usage-)
    - [III. Common Error That I found 📝](#iii-common-error-that-i-found-)
    - [IV. Official Website](#iv-official-website)
- [Contact](#contact-)

## Categories
 
#### I. Installation 🚀
1. Open PowerShell as Administrator
   ```sh
    wsl --install
   ```

2. Type your username dan password for WSL

3. Install Docker Desktop Configuration Check WSL2

4. Open VS Code You need install Visual Studio Code Extension (WSL from Extension Market Place)

5. open Terminal in VS code
6. Make Shared Folder (Because Ubuntu WSL is Virtual we need save our file into harddrive windows)

    ```sh
    sudo mkdir /mnt/project
    
    sudo mount -t drvfs '<Directory to mouth>' /mnt/project

    eg : sudo mount -t drvfs 'D:\Person\Data Dimas\17. Cloud WSL' /mnt/project
    ```

7. Change to Directory
    ```sh
    cd /mnt/project
    ```
8. Clone this repo 
    ```sh
    git clone https://github.com/didi2424/Tutorial-101-Random.git
    ```
9. Move to Directory jupyternotebookdocker
    ```sh
    cd '/Tutorial-101-Random/Docker 101/jupyternotebookdocker'
    ```
10. Build
     ```sh
    docker compose up
    ```

    
#### II. Usage 🧪

1. Open Docker Desktop in the Container Press Play Button

![](/Docker%20101/assets/dockerdesktopplay%20(1).gif)

2. Open Your Browser localhost:8000

![](/Docker%20101/assets/dockerdesktopplay%20(2).gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### III. Common Error That I found 📝

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





#### IV. Official Website
https://www.docker.com/products/docker-desktop/

https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64
https://www.nvidia.com/download/index.aspx

https://learn.microsoft.com/en-us/windows/wsl/install

## Contact 📞
[![WA][WA]][WA-url]

## Buy Me a Coffe ☕
<p align="center">
    <a href="" target="_blank">
        <img width="30%" src="/Docker 101/assets/binanceusdtwallet.jpg" alt="Banner">
    </a>
</p>


[🔼 Back to top](#How-to-install-Tensorflow-on-Docker-With-GPU-Compatible-Real-Time-Collaboration)


[WA]: https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white
[WA-url]: https://wa.me/085721977614