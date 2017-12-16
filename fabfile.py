#!/usr/bin/python
from fabric.api import *

def hello():
    print("Hello World!")

env.use_ssh_config = False
env.hosts = ["10.0.0.20"]
env.user = "root"
#env.key_filename = "/root/.ssh/id_rsa"
env.password = "Password!"
env.port = 22
 
 
def uptime():
        run("uptime")
        run ("ls -ltr")