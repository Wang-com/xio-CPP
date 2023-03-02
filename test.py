# import socket
#
# g_open = b"\xA0\x01\x00\xA1"
# g_close = b"\xA0\x01\x01\xA2"
#
# y_open = b"\xA0\x02\x01\xA3"
# y_close = b"\xA0\x02\x00\xA2"
#
# r_open = b"\xA0\x03\x01\xA4"
# r_close = b"\xA0\x03\x00\xA3"
#
# s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s1.settimeout(3)
# s1.connect(("192.168.2.196", 8080))
# s1.send(g_close)
# s1.close()

# import socket
# import time
# from threading import Thread
#
#
# class Client(Thread):
#
#     def __init__(self, port):
#         Thread.__init__(self)
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.client.settimeout(3)
#         self.client.connect(('192.168.2.201', port))
#         self.port = port
#
#     def run(self):
#         while True:
#             msg = str(self.port) + ': from client'
#             self.client.send(msg.encode('utf-8'))
#             time.sleep(0.5)
#
#
# for i in range(7):
#     port = 9090 + i
#     client = Client(port)
#     client.start()
#
# while True:
#     i = 4


# from opcua import Client
# from opcua import ua
# from opcua.common.node import Node
# from opcua.ua.uaerrors import BadNodeIdUnknown
#
# from socket import timeout
# import sys
# import cv2
#
# client = Client('opc.tcp://127.0.0.1:49320')
# try:
#     client.connect()
# except timeout:
#     raise TimeoutError("OPC服务器连接超时！")
# except Exception as e:
#     print(e)
#     print("OPC 服务器连接失败，系统自动退出！")
#     print("")
#     sys.exit(1)
#
# node = client.get_node('ns=2;s=sawanini1.CPU1215c.机器人安全触发')
#
# try:
#     value = node.get_value()
#     print(value)
#     node.set_attribute(ua.AttributeIds.Value,
#                        ua.DataValue(variant=ua.Variant(True)))
# except BadNodeIdUnknown:
#     raise RuntimeError("获取 {} 状态信息失败: 节点不存在！".format('salvagnini_1'))
#
# except Exception as e:
#     raise RuntimeError("获取 {} 状态信息失败: 未知错误！{}".format(node, e))

import cv2
from configs.config import video_stream_paths_dict

cap = {}
for name in video_stream_paths_dict.keys():
    path = video_stream_paths_dict[name]
    cap[name] = cv2.VideoCapture('rtsp://admin:hdu417417@192.168.2.10/Streaming/Channels/102')

i = 0
while True:
    for name in cap.keys():
        _, frame = cap[name].read()
        if frame is not None:
            # frame = cv2.resize(frame, (640, 480))
            cv2.imshow(name, frame)
            cv2.waitKey(1)

# import os
# import configparser

# config = configparser.ConfigParser()
# config.read("configs/dynamic_config.ini")
#
# print(config.options('site_interrupt_dict'))

# config.set('site_interrupt_dict', 'salvagnini_1', 'False')


# o = open("configs/dynamic_config.ini", 'w')
# config.write(o)
# print(config.getboolean('site_interrupt_dict', 'salvagnini_1'))






