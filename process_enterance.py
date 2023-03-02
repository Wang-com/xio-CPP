import time
import os
from multiprocessing import Process, Value
from main import gui_main
from handler.monitor import is_alive
from configs.config import check_detection_process_interval, reboot_time_steps


'''
:UPDATE_TIME 2022_3_23
把重启时间写入 D:\Project\epllo\logs\reboot_time.txt
'''
def output_reboot_time_2log(time):
    if not os.path.exists('D:\Project\epllo\logs'):
        os.mkdir('D:\Project\epllo\logs')
    with open('D:\Project\epllo\logs\\reboot_time.txt', 'a') as f:
        f.write('检测到重启，时间为：' + time + '\n')



def subprocess_run(detection_flag: Value) -> Process:
    p = Process(target=gui_main, args=(detection_flag,))
    p.start()
    return p


def main():
    detection_flag = Value('i', 0)  # variable(integer) with shared memory between multi processes
    p = subprocess_run(detection_flag)
    pre_time = time.time()
    while True:
        now_time = time.time()
        if now_time - pre_time > reboot_time_steps * 3600:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\t' + 'The detection process is <dead>!')
            p.terminate()  # kill the subprocess
            time.sleep(1)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\t' + 'reboot')
            detection_flag = Value('i', 0)
            p = subprocess_run(detection_flag)
            # added on 2022/3/23
            output_reboot_time_2log(now_time)
            pre_time = now_time

        time.sleep(check_detection_process_interval)
        if is_alive(detection_flag):
            print('The detection process is <alive>')
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\t' + 'The detection process is <dead>!')
            p.terminate()  # kill the subprocess
            time.sleep(1)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\t' + 'reboot')
            # added on 2022/3/23
            output_reboot_time_2log(now_time)
            detection_flag = Value('i', 0)
            p = subprocess_run(detection_flag)


if __name__ == '__main__':
    main()
