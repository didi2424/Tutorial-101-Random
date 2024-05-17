## How to install Tensorflow on Docker With GPU Compatible

<p align="center">
  This repository contains step how to build Tensorflow on Docker with GPU compitable. 
</p>

1. Powershell install WSL
   ```sh
    wsl --install
   ```

2. Type your username dan password for WSL

3. Install Docker Desktop Configuration Check WSL2

4. Open VS Code and open Terminal in VS code
 
5. Make Share Folder (Because Ubuntu WSL is Virtual we need save our file into harddrive windows)

    ```sh
    sudo mkdir /mnt/project
    
    sudo mount -t drvfs 'D:\Person\Data Dimas\17. Cloud WSL' /mnt/project
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
    FROM tensorflow/tensorflow latest-gpu

    WORKDIR /Dataset

    COPY requirments.txt requirments.txt 

    RUN pip install -r requirments.txt

    EXPOSE 8888

    ENTRYPOINT ['jupyter','lab',--ip=0.0.0.0, '--allow-root', '--no-browser']
    ```


8. Requitments txt
    ```sh
    code requirments.txt
    ```
    requirments.txt
    ```sh
    jupyterlab
    pandas
    matplotlib
    ```

9. Docker Compose YAML
    ```sh
    code docker-compose.yaml
    ```
    docker-compose.yaml
    ```sh
    version: '1.0'
    services:
        jupyter-lab:
          build: .
          ports:
            - '8888:8888'
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
10. buat direktori dataset didalam '/mnt/project'
    ```sh
    sudo mkdir dataset
    ```


11. Build
```sh
docker-compose up
```

## Common Error's That I found

### 1. During docker-compose up Warning 'docker-compose' could not be found

dimas@DESKTOP-D8N0KT4:/mnt/project$ docker-compose up

The command 'docker-compose' could not be found in this WSL 2 distro.
We recommend to activate the WSL integration in Docker Desktop settings.

For details about using Docker Desktop with WSL 2, visit:

https://docs.docker.com/go/wsl2/

#### Step to fix
  run docker in wsl terminal
  ```sh
  docker
  ```

### 2. During docker-compose up Error cuda>=12.3
Attaching to jupyter-lab-1
Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error running hook #0: error running hook: exit status 1, stdout: , stderr: Auto-detected mode as 'legacy'
nvidia-container-cli: requirement error: unsatisfied condition: cuda>=12.3, please update your driver to a newer version, or use an earlier cuda container: unknown


#### Step to fix
Download and update Cuda Version on Windows

https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64