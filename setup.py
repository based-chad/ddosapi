
import os
import subprocess

os.system("clear")

print("\033[1;36m [+] Recomended to be ran in a Virtual Enviorment \n")

sudo=input("\033[1;34m Do you want sudo privilages (y/n): ")
c = "UHJvZ3JhbW1lZCBieSBiYXNlZC1jaGFkLiBodHRwczovL2dpdGh1Yi5jb20vYmFzZWQtY2hhZCwgSUcgQFNraWRzLkNyeWluZw=="
if sudo == 'y':
    subprocess.run("sudo mkdir skid_stuff ;cd skid_stuff",shell=True)
    subprocess.run("sudo apt update ; sudo apt upgrade",shell=True)
    subprocess.run("sudo apt install python3.10",shell=True)
    subprocess.run("sudo apt install python3-pip",shell=True)
    subprocess.run("sudo apt install git",shell=True)
    subprocess.run("pip3 install flask",shell=True)
    os.system("clear")
    print("\033[1;31m [+] Setup Done! You are a complete Skid Now.")
    print("\033[1;31m [+] Keep in mind when you want to deploy this, you might need to open some ports on your server. What a YouTube tutorial on (How to deploy a flask app on VPS server.)")

elif sudo == 'n':
    subprocess.run("mkdir skid_stuff ;cd skid_stuff",shell=True)
    subprocess.run("apt update ; sudo apt upgrade",shell=True)
    subprocess.run("apt install python3.10",shell=True)
    subprocess.run("apt install python3-pip",shell=True)
    subprocess.run("sudo apt install git",shell=True)
    subprocess.run("pip3 install flask",shell=True)
    os.system("clear")
    print("\033[1;31m Setup Done! You are a complete Skid Now.")
    print("\033[1;31m [+] Keep in mind when you want to deploy this, you might need to open some ports on your server. What a YouTube tutorial on (How to deploy a flask app on VPS server.)")

else:
    print("exit")
    exit()


