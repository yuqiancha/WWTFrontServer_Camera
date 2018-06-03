import http.client
import time
import threading
from Data import MyLock
from Data import SharedMemory
from PyQt5 import QtCore
from PyQt5.QtCore import *
import urllib.parse
import logging.config
from os import path
import socket
from binascii import hexlify,unhexlify
import json
import struct

MyLog2 = logging.getLogger('ws_debug_log2')       #log data
MajorLog = logging.getLogger('ws_error_log')      #log error

class TcpClient(QThread):
    signal_detect = pyqtSignal(str)
    signal_showID = pyqtSignal(str)
    def __init__(self):
        super(TcpClient,self).__init__()
        print("TcpClient In")

        self.ThreadTag = True

        server_ip = '192.168.0.98'
        server_port = 9740

        MySocket = self.ConnectCamera(server_ip,server_port)

        t = threading.Thread(target=RecvFromCamera, args=(MySocket,self))
        t.start()

        t2=threading.Thread(target = SendToCamera,args=(MySocket,self))
        t2.start()

    def ConnectCamera(self,server_ip,server_port):

        tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        try:
            tcp_client.connect((server_ip,server_port))
        except:
            pass
        return tcp_client


    def close(self):
        self.ThreadTag = False

def SendToCamera(Mysocket,self):
    print("SendToCamera In")
    CameraNeedInitTag = True

    while self.ThreadTag:
        if CameraNeedInitTag:
            Mysocket.send('EP'.encode() + unhexlify('060000000000') + '[setfmt]\nfmt = bin\n'.encode())
            time.sleep(0.2)
            #    sockLocal.send('EP'.encode() + unhexlify('070000000000'))
            CameraNeedInitTag = False

        msg = 'EP'.encode() + unhexlify('050000000000')
        Mysocket.send(msg)
        time.sleep(1)



def RecvFromCamera(Mysocket,self):
    print('RecvFromCamera In')

    while self.ThreadTag:
        try:
            RecvStr = Mysocket.recv(16384*16)

            Thead,Ttype,Treserved=struct.unpack("!2sBB",RecvStr[0:4])
            Tlenth, = struct.unpack("<I",RecvStr[4:8])

            if Thead==b'EP':
                #print('1:', Thead, Ttype, Treserved, Tlenth)
                RecvStr = RecvStr[8:] #去掉总包头
                Index = 0

                while Index<Tlenth:
                    Shead,SType,Sreserved=struct.unpack("!2sBB",RecvStr[0:4])
                    Slenth, = struct.unpack("<I", RecvStr[4:8])

                    #print('2:',Shead,SType,Sreserved,Slenth)

                    if Shead==b'EP' and SType==11:
                    #    print("Recved Heart!")
                        Index +=8
                    if Shead==b'EP' and SType==1:
                        print("Recved 识别信息find")
                        Mid,Mcount=struct.unpack("<ii",RecvStr[8:16])
                        print(Mid, Mcount)
                        y, m, d, hh, mm, ss = struct.unpack("<iiiiii", RecvStr[16:40])
                        print(y, m, d, hh, mm, ss)

                        pos=40

                        license,color=struct.unpack("!16s8s",RecvStr[pos:pos+24])
                        nColor, nType, nConfigdence, rec_time = struct.unpack("<iiii",RecvStr[pos+24:pos+40])
                        license_de = '车牌号:'
                        license_de+=license.decode('gbk')
                        license_de = license_de.split('\x00')[0]
                        color_de = '颜色:'
                        color_de += color.decode('gbk')
                        color_de = color_de.split('\x00')[0]
                        #print(license,color,nColor,nType,nConfigdence,rec_time)
                        print(license_de,color_de)
                        MajorLog.info(license_de+color_de)
                        Index +=8+824

                        DColor = color_de.split(':')[1]
                        if DColor=='绿':
                            self.signal_detect.emit('0501')
                            self.signal_showID.emit(license_de.split(':')[1])
                            print("触发显示:"+license_de.split(':')[1])

                        break

        except socket.error:
            print('socket error,do reconnect')
            time.sleep(3)
#            sockLocal = self.ConnectCamera(server_ip, server_port)
        except Exception as ex:
            print('other error occur :')
            print(ex)
            time.sleep(3)

    print('Exit RecvFromCamera')
    pass