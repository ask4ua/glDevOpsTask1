# Intro
getres.py - just a tool to get CPU and RAM utilization for fun;)

Available either containered in Docker or as native script.

## How to run in Docker
### How to build docker image with getres
As prerequizite docker should be installed. Follow by this guides if needed: 

Steps:
1) Checkout the repo: 

        git clone https://github.com/ask4ua/glDevOpsTask1

2) Navigate to the root directory of your local repo:

        cd glDevOpsTask1/
        
3) Execute docker build with such options:

        docker build . -t getres -f docker/Dockerfile
    
    Check docker image **getres** is created:
    
        docker image ls
        
        REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
        getres                       latest              2d78f7077655        44 seconds ago      937MB
        docker.ask4ua.com/whir-app   latest              3f4e6630f268        20 hours ago        416MB
        ...       
### How to tun in docker
To run execute such command for Memory monitoring:

        docker run --rm getres mem
        
        user@k8s1:~/GIT/glDevOpsTask1$ docker run --rm getres mem
        virtual total 6250455040
        virtual available 4462530560
        virtual percent 28.6
        ...
        
and for cpu:

        docker run --rm getres cpu
        
        system.cpu.user 5950.5
        system.cpu.nice 0.0
        system.cpu.system 5970.06
        system.cpu.idle 216346.9
        ...    
        
Enjoy!)

## How to run natively (without Docker)
As prerequizites python3 and psutils package should be installed on executing host.

The script getres.py provides in response cpu or memory resource utilization.
Only 1 parameter is acceptable in a time.

    getres.py [cpu|mem]
    
Where:
- cpu - prints CPU metrics
- mem - prints RAM metrics

getres.py is stored in folder app of Git repo.
Could be moved as standalone ./app to any other location.

Examples of usage:
1) Get memory usage:

        user@k8s1:~/GIT/glDevOpsTask1$ user$ python3 getres.py mem
        virtual total 8589934592
        virtual available 2547195904
        virtual percent 70.3
        ...
    
2) Get CPU usage:

        user@k8s1:~/GIT/glDevOpsTask1$ python3 app/getres.py cpu
        system.cpu.user 50323.99
        system.cpu.nice 0.0
        system.cpu.system 49587.98
        system.cpu.idle 367804.51
        
       
# Docker versus Native
Docker and native ways could show different values for some circumstates like executing on Mac OS due to external dockerd limits on MacOS settings.
But for linux hosts values should be the same (with difference only for the system state on the execution moment).
