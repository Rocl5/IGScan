import queue
import threading
import time

import requests
import requests.packages.urllib3

from utils.util import get_random_headers

requests.packages.urllib3.disable_warnings()  #


class RequestsURL(object):
    def __init__(self):
        self.sub_file = 'output/subdomain.txt'
        self.link_file = 'output/link.txt'
        self.link_num = 0
        self.sub_q = queue.Queue()  # 放置子域名的队列
        self.survival_q = queue.Queue()  # 放置存活域名的队列，用于写入result.txt
        self.headers = {"User-Agent": get_random_headers()}

    def get_url(self, total_num):
        start_time = time.time()
        while not self.sub_q.empty():
            get_url = self.sub_q.get()
            end_time = time.time()
            program_time = (end_time - start_time)  # 运行时长
            threading.Thread(target=self.progress, args=(total_num, program_time)).start()
            try:
                for scheme in ['http', 'https']:
                    http_url = "{}://".format(scheme) + get_url

                    http_res = requests.get(url=http_url, headers=self.headers, timeout=1, verify=False)
                    if http_res.status_code == 200:
                        self.survival_q.put(http_url)
                        self.link_num += 1  # 计数有多少link
            except Exception as e:
                pass

    def progress(self, total_num, _time):
        """
        :param _time:
        :param total_num: 所有待检测子域名的数量
        :return:
        """
        # 用putsubdomain这个队列做进度条，使用总数减去则为当前已检测的num
        get_num = total_num - self.sub_q.qsize()  # 已检测的域名数量
        # 公式 alltime = allcheck * nowtime / nowcheck
        Remaining_time = (total_num * time / get_num) - _time  # 程序剩余运行时间 预计总时间-已运行时间
        if total_num >= 100:
            print('\r\033[34m[PROG]\033[0m Detected: %d Progress: %.2f %% Time: %.1fs The Remaining time: %.1fs' %
                  (get_num, (get_num / total_num * 100), _time, Remaining_time), end="")
        else:
            print('\r\033[34m[PROG]\033[0m Detected: %d Progress: %.2f %% '
                  % (get_num, (get_num / total_num * 100)), end="")

    def url_run(self):
        print('\033[34m[INFO]\033[0m CheckDomain Module Running!')
        thread_list = []
        with open(self.sub_file, 'r') as f:
            for subdomain in f.readlines():
                self.sub_q.put(subdomain.strip('\n'))
        total_num = self.sub_q.qsize()  # 获取子域名的总数
        for i in range(50):
            t = threading.Thread(target=self.get_url, args=(total_num,))
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        f = open(self.link_file, 'w')
        while not self.survival_q.empty():
            put_url = self.survival_q.get()
            f.write(put_url + '\n')
        f.close()
        print('\n\033[032m[SUCC]\033[0m CheckDomain Module Has Finished Running!')
        print('\033[034m[INFO]\033[0m The number of links obtained is: %d' % self.link_num)

    def file_start(self, targets_file):
        print('\033[34m[INFO]\033[0m CheckDomain Module Running!')
        if targets_file != '' and targets_file != None:
            thread_list = []
            with open(targets_file, 'r') as f:
                for subdomain in f.readlines():
                    self.survival_q.put(subdomain.strip('\n'))
            total_num = self.survival_q.qsize()  # 获取子域名的总数
            for i in range(50):
                t = threading.Thread(target=self.get_url, args=(total_num,))
                thread_list.append(t)
            for t in thread_list:
                time.sleep(0.01)
                t.start()
            for t in thread_list:
                t.join()
            f = open(self.link_file, 'w')
            while not self.survival_q.empty():
                put_url = self.survival_q.get()
                f.write(put_url + '\n')
            f.close()
            print('\n\033[032m[SUCC]\033[0m CheckDomain Module Has Finished Running!')
            print('\033[034m[INFO]\033[0m The number of links obtained is: %d' % self.link_num)
