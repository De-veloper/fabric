#!/usr/bin/python
from fabric.api import *
def hello():
    print("Hello World!")

env.use_ssh_config = False
env.hosts = ["localhost"]
#env.user = ""
#env.key_filename = "/root/.ssh/id_rsa"
env.password = ""
#env.port = 22
 
 
def uptime():
    run("uptime")
    run ("ls")
