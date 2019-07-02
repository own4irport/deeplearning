import gzip

from datetime import datetime
import time
import os
import shutil



def zip_log(env_device=None):
    if env_device is not None:
        # 抓取log
        if os.path.exists(r"d:/tv_log/android_logs"):
            if not os.listdir(r"d:/tv_log/android_logs"):
                os.rmdir(r"d:/tv_log/android_logs")
            else:
                shutil.rmtree(r"d:/tv_log/android_logs")
        cmd_text = "-s " + env_device + " pull data/log/android_logs d:/tv_log/android_logs"
        self.cmd.cmd(cmd_text)
        time.sleep(2)
    gz_file_name = ""
    # 解压log
    for f_file_path, c_dir, c_file in os.walk(self.hd_log_path):
        if len(c_file) == 0:
            pass
        else:
            hd_log_path = os.path.join(self.hd_log_path, "android_logs")
            for c_file_name in c_file:
                if "applogcat" in c_file_name:
                    gz_file_name = os.path.join(hd_log_path, c_file_name)
    print(gz_file_name)
    f_name = gz_file_name.replace(".gz", "")
    print(gz_file_name)

    # 获取文件的名称，去掉
    g_file = gzip.GzipFile(gz_file_name)
    # 创建gzip对象
    with open(f_name, "w", encoding="utf-8", errors="ignore") as f:
        f.write(str(g_file.read(), encoding="utf-8", errors="ignore"))
    g_file.close()
    print(f_name)
    return f_name


def call_start_time(order_time=None, env_device=None):
    """
    视频通话接通时延
    :param env_device: 设备所在环境
    :return:
    """
    f_name = "./applogcat-log.I000.20190514-110040"
    hd_start = "open camera"
    # hd_stop = "huawei Tv miracast device up"
    hd_start_time = ""
    hd_stop_time = order_time
    hd_connect_start_flag = False
    hd_connect_stop_flag = False
    with open(f_name, "r", encoding="utf-8", errors="ignore") as f:
        for line in f.readlines():
            if hd_start in line and hd_connect_start_flag is False:
                line_list = line.split(" ")
                print(line_list)
                value = str(datetime.now().year) + "-" + line_list[0] + " " + line_list[1]
                hd_start_time = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
                print(hd_start_time)
                hd_connect_start_flag = True
            # elif hd_stop in line and hd_connect_stop_flag is False:
            #     line_list = line.split(" ")
            #     value = str(datetime.now().year) + "-" + line_list[0] + " " + line_list[1]
            #     hd_stop_time = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
            #     hd_connect_stop_flag = True
    if hd_connect_start_flag:
        hd_stop_time = datetime.strptime(order_time, '%Y-%m-%d %H:%M:%S.%f')
        start_time = str(hd_stop_time - hd_start_time).split(":")[-1]
        print("发现投屏器时延为 %s" % start_time)
        return round(float(start_time), 3)
    else:
        return 0


if __name__ == '__main__':
    # time_01 = call_start_time(order_time=str(datetime.now().__format__('%Y-%m-%d %H:%M:%S.%f')))
    # print(time_01)
    # hd_start_time = datetime.strptime("2019-05-29 15:28:31.666000", '%Y-%m-%d %H:%M:%S.%f')
    # hd_end_time = datetime.strptime("2019-05-29 15:28:33.666000", '%Y-%m-%d %H:%M:%S.%f')
    # print(hd_end_time - hd_start_time)
    # print(str(hd_end_time - hd_start_time).split(":")[-2])
    # print(datetime.now())
    time1 = datetime.now()
    print(datetime.now())
    time2 = hd_start_time = datetime.strptime(time1, '%Y-%m-%d %H:%M:%S.%f')