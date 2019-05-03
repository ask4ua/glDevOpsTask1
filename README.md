# Intro
getres.py - just a containered tool to get CPU and RAM utilization for fun;)

## How to run natively ()without Docker)
The script getres.py provides in response cpu or memory resource utilization.
Only 1 parameter is acceptable in a time.

    getres.py [cpu|mem]
    
Where:
- cpu - prints CPU metrics
- mem - prints RAM metrics

getres.py is stored in folder app of Git repo.
Could be moved as standalone app to any other location.

Examples of usage:
1) Get memory usage:

        t00l:dir user$ python3 getres.py mem
        virtual total 8589934592
        virtual available 2547195904
        virtual percent 70.3
        ...
    
2) Get CPU usage:

        t00l:dir user$ python3 getres.py cpu
        system.cpu.user 44469.61
        system.cpu.nice 0.0
        system.cpu.system 43812.96
        system.cpu.idle 322224.82

## How to run in Docker
### How to build docker image with getres
As prerequizite docker should be installed. Follow by this guide if needed: <https://docs.docker.com/get-started/>

Steps:
1) Checkout the repo: 
2) Navigate to the root directory of your local repo.
3) Execute docker build with such options:

        docker build . -t getres -f docker/Dockerfile
    
    Check docker image **getres** is created:
    
        t00l:glDevOpsTask1 volk$ docker image ls
        
        REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
        getres                       latest              2d78f7077655        44 seconds ago      937MB
        docker.ask4ua.com/whir-app   latest              3f4e6630f268        20 hours ago        416MB
        ...       

### How to use getres in docker image
Check you have retrieved an image and loaded it:

    t00l:glDevOpsTask1 volk$ docker image ls | grep getres
    getres                       latest              ff97a55c3d03        7 minutes ago       937MB

If not loaded - use this instruction how to load custom docker images

Just run container as cpu or mem parameter:

    t00l:dir user$ docker run --rm getres cpu
    system.cpu.user 5727.66
    system.cpu.nice 0.0
    system.cpu.system 5593.73
    ...

### How it is working in Docker
TBD for:

There are several challenges you may face:
 - How to display information about processes running on the host machine from within container environment (think about pid namespaces).
 - How to display usernames for processes running on the host machine from within container environment (think how linux resolves uid to username and docker volumes).
