import socket
import sys
import os
from time import sleep

READY_SERVER_PORT = 3000
READY_CLIENT_PORT = 6000
PORT = 1337
SERVER_NAME = "localhost"

SYN_PORT_1 = 9000
SYN_PORT_2 = 9001
SYN_PORT_3 = 9002
BIT_PORT = 9003

def try_socket(port = PORT):
    sock = socket.socket()
    sock.bind((SERVER_NAME,port))
    sock.close()
    
def create_socket(port = PORT):
    try:
        sock = socket.socket()
        sock.bind((SERVER_NAME,port))
        return sock
    except:
        pass
    return sock

def is_busy(port = READY_SERVER_PORT):
    try:
        sock = socket.socket()
        sock.bind((SERVER_NAME,port))
        sock.close()
    except:
        return 1
    else:
        return 0



if __name__ == "__main__":
    
    file_name = sys.argv[1]
    if not os.path.exists(file_name) or sys.argv[1] == None:
        print("Error: file not found!")
        exit(1)
        
    server = create_socket(READY_SERVER_PORT)
    print("Server is ready")
    
    print("Waiting for client")
    
    while True:
        try:
            try_socket(READY_CLIENT_PORT)
        except:
            break
    
    print("Start to transfering")    
    in_file = open(file_name, "rb")
    size = os.path.getsize(file_name)
    out_bytes = 0
    while True:
        byte = in_file.read(1)
        if not byte:
            break
        mask = 0b10000000
        for i in range(8):  
            bit = byte[0] & mask
            if bit:
                if not is_busy(BIT_PORT):
                    bit_sock = create_socket(BIT_PORT)
                print(1)
            else:
                if is_busy(BIT_PORT):
                    bit_sock.close()
                print(0)
            mask >>= 1
            #Даем сигнал на ресив и ждем другого сигнала
            syn = create_socket(SYN_PORT_1)
            #input("Ждем")
            sleep(0.00000000000000000000000000001)
            while is_busy(SYN_PORT_1):
                if is_busy(SYN_PORT_2):
                    syn.close()
        out_bytes += 1
        #print(str(int((out_bytes*100)/size))+'%')
            
            
    server.close()
    in_file.close()
    print("Finished")
