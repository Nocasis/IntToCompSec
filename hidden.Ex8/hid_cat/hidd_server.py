from sys import argv
import os

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

if __name__ == "__main__":

    if len(argv) != 2:
        print("Incorrect argv!")
        print("Usage:python3 {} file_name".format(argv[0]))
        exit(1)

    file_name = argv[1]
    if not os.path.exists(file_name):
        print("file not found!")
        exit(1)
        
    create_file(READY_SERVER_FILE)
    print("Server is ready.")
    
    print("Waiting for client.")
    
    while not os.path.exists(READY_CLIENT_FILE):
        pass
    
    print("Starting to transfer.")    
    server_file = open(file_name, "rb")
    size = os.path.getsize(file_name)
    out_bytes = 0
    create_file(ONLINE_FILE)
    
    while os.path.exists(READY_CLIENT_FILE):
        byte = server_file.read(1)
        if not byte:
            break
        mask = 0b10000000
        for i in range(8):  
            bit = byte[0] & mask
            if bit:
                create_file(BIT_FILE)
                #print(1)
            else:
                 delete_file(BIT_FILE)
                 #print(0)

            mask >>= 1
            create_file(SYN_FILE)
            #input("ждем")
            while os.path.exists(SYN_FILE):
                pass

        out_bytes += 1
        percent = int((out_bytes*100)/size)
        decorate(percent)
    
    delete_file(READY_SERVER_FILE)
    delete_file(ONLINE_FILE)
    delete_file(BIT_FILE)
    server_file.close()
    print("\nTransfer is finished!")
