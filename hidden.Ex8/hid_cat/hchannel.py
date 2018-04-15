#!/usr/bin/python3
BIT_FILE = "bit"
ONLINE_FILE = "online"
SYN_FILE = "syn"
READY_SERVER_FILE = "ready_server"
READY_CLIENT_FILE = "ready_client"

def create_file(file_name):
    if not os.path.exists(file_name):
        _file_ = open(file_name, "w")  
        _file_.close()

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        
def decorate(percent):
    os.system("clear")
    print("Tranfer:")
    count = int(percent/5)
    line = "|"
    for i in range(20):
        if i < count:
            line += '='
        else:
            line += ' '
    line += '|'
    print("          {}%          ".format(percent))
    print(line)

