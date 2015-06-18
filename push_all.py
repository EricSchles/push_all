import os
from sys import argv
from subprocess import call
def pushing():
    call(["git","add","-A",":/"])
    call(["git","commit","-a","-m",'"Updating anything that was missing"'])
    call(["git","push"])
for root,dirs,files in os.walk(argv[1]):
    #print dirs
    os.path.exists(".git")
    for Dir in dirs:        
        original = os.getcwd()
        os.chdir(os.path.join(os.getcwd(),root,Dir))
        if os.path.exists(".git"):
            pushing()
        os.chdir(original)
