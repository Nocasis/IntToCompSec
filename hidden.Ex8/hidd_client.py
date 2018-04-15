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
    return None

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
    client = create_socket(READY_CLIENT_PORT)
    print("Client is ready")
    
    print("Waiting for server")
    
    while True:
        try:
            try_socket(READY_SERVER_PORT)
        except:
            break
    
    print("Start to reciving")    
    out_file = open(file_name, "wb")
    bytearr = bytearray()
    while is_busy(READY_SERVER_PORT):
        byte = 0
        
        
        for i in range(8):
            #Ждем сигнала
            while not is_busy(SYN_PORT_1) and is_busy(READY_SERVER_PORT):
                pass
            #input("Ждем в начале") 
            if is_busy(BIT_PORT):
                byte <<= 1
                byte |= 1
                print (1)
            else:
                byte <<= 1
                print(0)
                
            #отправляем сигнал
            #while True:
            #    syn = create_socket(SYN_PORT_2)
            #    if syn != None:
            #        break
            #sleep(1)
            #syn.close()
            while is_busy(SYN_PORT_1):
                try:
                    syn = create_socket(SYN_PORT_2)
                    syn.close()
                    if not is_busy(SYN_PORT_1):
                           break
                except:
                    pass
            
        if not is_busy(READY_SERVER_PORT):
            break;   
        bytearr.append(byte)

    #bytearr.pop()
    out_file.write(bytearr)
    out_file.close()
    client.close()
    print("Finished")
