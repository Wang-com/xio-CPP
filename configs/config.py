switch_dict = {
    'line_1_rush': True,
    'line_1_1': True,
    'line_2_rush': True,
    'line_2_1': True,
    'line_2_2': True,
    'line_1_2': True,
    'line_weld': True
}

site_interrupt_dict = {
    'line_1_rush': True,
    'line_1_1': True,
    'line_2_rush': True,
    'line_2_1': True,
    'line_2_2': True,
    'line_1_2': True,
    'line_weld': True
}

pre_dict = {
    'line_1_rush': False,
    'line_1_1': False,
    'line_2_rush': False,
    'line_2_1': False,
    'line_2_2': False,
    'line_1_2': False,
    'line_weld': False
}

signal_dict = {
    'line_1_rush': 0,
    'line_1_1': 0,
    'line_2_rush': 0,
    'line_2_1': 0,
    'line_2_2': 0,
    'line_1_2': 0
}

name_array = [
    'line_1_rush',
    'line_1_1',
    'line_2_rush',
    'line_2_1',
    'line_2_2',
    'line_1_2',
    'line_weld'
]

off_signal_dict = {
    'line_1_rush': 0,
    'line_1_1': 0,
    'line_2_rush': 0,
    'line_2_1': 0,
    'line_2_2': 0,
    'line_1_2': 0,
    'line_weld': 0
}

station_name_dict = {
    'line_1_rush': '厚板线1-冲',
    'line_1_1': '厚板线1-折1',
    'line_2_rush': '厚板线2-冲',
    'line_2_1': '厚板线2-折1',
    'line_2_2': '厚板线2-折2',
    'line_1_2': '厚板线1-折2',
    'line_weld': '厚板线2-焊'
}

station_name_switch_dict = {
    'line_1_rush': '厚板线1-冲√',
    'line_1_1': '厚板线1-折1√',
    'line_2_rush': '厚板线2-冲√',
    'line_2_1': '厚板线2-折1√',
    'line_2_2': '厚板线2-折2√',
    'line_1_2': '厚板线1-折2√',
    'line_weld': '厚板线2-焊√'
}

site_1 = 'line_1_rush'
site_2 = 'line_1_1'
site_3 = 'line_2_rush'
site_4 = 'line_2_1'
site_5 = 'line_2_2'
site_6 = 'line_1_2'
site_7 = 'line_weld'

dynamic_config_path = 'configs/dynamic_config.ini'
interrupt_switch_section = 'site_interrupt_dict'

video_stream_paths_dict = {
    'line_1_rush': 'rtsp://admin:hdu417417@192.168.2.176/Streaming/Channels/101',
    'line_1_1': 'rtsp://admin:hdu417417@192.168.2.50/Streaming/Channels/101',
    'line_2_rush': 'rtsp://admin:hdu417417@192.168.2.173/Streaming/Channels/101',
    'line_2_1': 'rtsp://admin:hdu417417@192.168.2.175/Streaming/Channels/101',
    'line_2_2': 'rtsp://admin:hdu417417@192.168.2.171/Streaming/Channels/101',
    'line_1_2': 'rtsp://admin:hdu417417@192.168.2.51/Streaming/Channels/101',
    'line_weld': 'rtsp://admin:hdu417417@192.168.2.174/Streaming/Channels/101'
}

masks_paths_dict = {
    'line_1_rush': 'images/masks/mask_1_rush.jpg',
    'line_1_1': 'images/masks/mask_1_1.jpg',
    'line_2_rush': 'images/masks/mask_2_rush.jpg',
    'line_2_1': 'images/masks/mask_2_1.jpg',
    'line_2_2': 'images/masks/mask_2_2.jpg',
    'line_1_2': 'images/masks/mask_1_2.jpg',
    'line_weld': 'images/masks/mask_2_weld.jpg'
}

max_object_bbox_area_dict = {
    'line_1_rush': 15000,
    'line_1_1': 15000,
    'line_2_rush': 15000,
    'line_2_1': 15000,
    'line_2_2': 15000,
    'line_1_2': 5000,
    'line_weld': 15000
}


# OPC 服务器 URL
opc_url = 'opc.tcp://127.0.0.1:49320'

# 是否连接OPC服务器，执行紧急停机
open_opc =True
# 开启邮箱OPC报警
open_email_warning = False
# 开启统计闯入次数和邮箱发送报告功能
open_email_report = False
# 开启数据库存储异常记录
open_mysql_save_record = False

mysql_interrupt_table = 'interrupt_cpp'

# nodes_dict = {
#     'line_1_rush': 'ns=2;s=sawanini1.CPU1215c.机器人安全触发',
#     'line_1_1': "ns=2;s=sawanini2.Q.机器人安全触发",
#     'line_2_rush': "ns=2;s=tongyong2chongzhe1.s7300.冲床机器人安全检查触发",
#     'line_2_1': "ns=2;s=tongyong2chongzhe1.s7300.折弯1机器人安全检查触发",
#     'line_2_2': "",
#     # 'line_1_2': "ns=2;s=pumbjiaobi.Q.机器人安全触发",
#     'line_1_2': "",
#     'line_weld': ""
# }

nodes_dict = {
    'line_1_rush': 'ns=2;s=厚板1自动线.厚板1冲折机器人安全监控.冲机器人安全触发',
    'line_1_1': "ns=2;s=厚板1自动线.厚板1冲折机器人安全监控.折1机器人安全触发",
    'line_2_rush': "ns=2;s=厚板2冲床折弯1.冲折1机器人安全监控.冲机器人安全监测触发",
    'line_2_1': "ns=2;s=厚板2冲床折弯1.冲折1机器人安全监控.折弯1机器人安全监测触发",
    'line_2_2': "ns=2;s=厚板2折弯2.厚板2折弯机2机器人安全监控.折弯2机器人安全触发",
    'line_1_2': "ns=2;s=厚板1自动线.厚板1冲折机器人安全监控.折2机器人安全触发",
    'line_weld': "ns=2;s=厚板2焊接.焊接机器人安全监控.焊接机器人安全监控触发"
}

min_object_bbox_area_dict = {
    'line_1_rush': 500,
    'line_1_1': 850,
    'line_2_rush': 500,
    'line_2_1': 500,
    'line_2_2': 500,
    'line_1_2': 500,
    'line_weld': 600
}

excluded_objects_dict = {
    'line_1_rush': [[415, 162, 459, 125], [266, 325, 289, 355], [254, 311, 297, 348], [254, 291, 287, 330],
                    [238, 264, 296, 357], [236, 414, 279, 446], [321, 0, 397, 64]],
    'line_1_1': [],
    'line_2_rush': [[303, 160, 323, 230], [371, 138, 410, 153], [398, 95, 413, 147], [405, 156, 436, 208]],
    'line_2_1': [[481, 230, 498, 247], [443, 286, 454, 299], [490, 267, 509, 281], [481, 258, 507, 295],
                 [58, 339, 83, 356], [397, 169, 426, 197], [357, 274, 396, 329], [337, 129, 361, 205]],
    'line_2_2': [],
    'line_1_2': [],
    'line_weld': [[255, 300, 284, 330], [204, 161, 229, 189], [499, 146, 508, 187], [294,234, 317, 277],
                  [576, 142, 605, 190], [160, 141, 197, 198], [157, 278, 186, 328], [167, 215, 211, 282],
                  [113, 237, 152, 316], [264, 209, 338, 265], [153, 251, 191, 312], [358, 212, 402, 282],
                  [159, 256, 205, 355]]
}
# 330, 179 356, 221

frame_shape = (480, 640)

vis_name = 'line_2_2'
prev_vis_name = vis_name

device_name = 'cuda:0'
img_size = 640  # size of each image dimension
config_path = 'yolox/configs/yolox_m.py'  # path to model configs file
# 如果出现检测问题需要回滚，把下面这行注释掉
# weight_path = 'yolox/configs/best_ckpt.pth'
weight_path = 'yolox/configs/best_ckpt.pth'
# 如果出现检测问题需要回滚，把下面这行注释打开
# weight_path = 'ckpt-backup-2022-4-12/best_ckpt.pth'
conf_thres = 0.65  # object confidence threshold
nms_thres = 0.75  # iou threshold for non-maximum suppression

mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = '123456'
mysql_db = 'xio'

email_opc_warning_interval = 3600


wechat_send_interval = 30

inter_threshold = 0.15

open_wechat_bot = False

wechat_group = "机器人安全监测"

report_statistics_interval = 3600

server_name_dict = {
    'line_1_rush': '192.168.2.88',
    'line_1_1': '192.168.2.166',
    'line_2_rush': '192.168.2.78',
    'line_2_1': '192.168.2.72',
    'line_2_2': '192.168.2.82',
    'line_1_2': '192.168.2.53',
    'line_weld': None
}

server_port = 8080

# server_name = '192.168.2.201'
#
# server_port_dict = {
#     'line_1_rush': 9090,
#     'line_1_1': 9091,
#     'line_2_rush': 9092,
#     'line_2_1': 9093,
#     'line_2_2': 9094,
#     'line_1_2': 9095,
#     'line_weld': 9096
# }

alarm_link_success = 0
alarm_link_failed = 1

check_detection_process_interval = 65

update_detection_flag_interval = 20

reboot_time_steps = 24

alarm_instruction = True


