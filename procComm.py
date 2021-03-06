#!/usr/bin/python           # This is server.py file
import os
import sys
from threading import Thread
import multiprocessing
import socket               # Import socket module
from slackclient import SlackClient
from botMap import *


IS_SLACK= True
#s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
#port = 50000                # Reserve a port for your service.
#SocketServer server
class procComm:
    HOST = 0; #ocket.gethostbyname(socket.gethostname())
    port = 0
    server = 0
    IS_DATA = 0
    IS_CMD = 1
    def __init__(self,token,port):
        if(IS_SLACK == True):
            self.server = SlackClient(token)
        else:
            self.port = port
            self.server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind((self.HOST,  self.port))
            sys.stderr.write('Msg Bind: '+str(self.port)+'\n')

    def procMsgEx(self,data):
        for AT_BOT in BOT_MSG_HEAD:
            if data.startswith(AT_BOT):
                sys.stderr.write('[*] msgEx:'+str(BOT_MAP[AT_BOT][0]))
                self.procMsgSend(channel = BOT_MAP[AT_BOT][0],text = data,dataType = 0)
                ret = self.procMsgRecv()
                ret[0]['channel'] = BOT_MAP[AT_BOT][0]
                return ret[0]['text'],ret[0]['channel']
        return '',0
        
    def procMsgConn(self):
        if(IS_SLACK == True):
            return self.server.rtm_connect()
        else:
            return True
            
    def procMsgRecv(self):
        #print('Msg Recv')
        if(IS_SLACK == True):
            return self.server.rtm_read()
        else:           
            output_list = []
            # self.request is the UDP socket connected to the client
            data = self.server.recv(1024).strip()
            sys.stderr.write('Msg Recv Data on '+str(self.server.getsockname())+' data: '+data +'\n')
            output_list.append({'text':data,'channel':IS_MSG_HANDLER_PORT})
            return output_list
        
    def procMsgSend(self,channel,text,dataType):
        port = channel
        if(IS_SLACK == True):
            self.server.api_call("chat.postMessage", channel=channel,text=text, as_user=True)
        else:
            sys.stderr.write('Msg Send on '+str(self.server.getsockname())+ ' to ' + str(port)+'\n')
            server_address = (self.HOST, port)
            self.server.sendto(bytes(text + '\n'),server_address)
            #print("Sent:     {}".format(data))
    
def procMsgInit(token,port):
    sys.stderr.write('Msg init\n')
    obj = procComm(token,port)
    return obj
