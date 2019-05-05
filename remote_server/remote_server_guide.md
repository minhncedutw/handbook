## Remote connections
```commandline
ssh sofin@140.124.30.118 # access
ssh -L 8888:localhost:8888 ACCOUNT@SERVER_IP # access and connect local port to remote port
sudo netstat -tupn # check remote internet tcp connections
sudo kill -9 IP # close remote tcp connections
```

## Remote gpu
```commandline
nvidia-smi # show gpu performance
sudo kill -9 IP # close gpu session
```
