import os
import queue
import threading
import time

from core.get_subdomain import GetSub
from utils.util import get_random_headers


class GetSubDomain(GetSub):
    def __init__(self):
        super(GetSub).__init__()
        self.subdomain_num = 0
        if not os.path.exists('output'):
            os.mkdir('output')
        self.sub_file = open('output/subdomain.txt', 'w')
        self.domain_q = queue.Queue()
        self.queue = queue.Queue()
        self.headers = {"User-Agent": get_random_headers()}

    # -u参数
    def get_subdomain(self, domain):
        li = []
        print('\033[034m[INFO]\033[0m GetDomain Module Running!')
        for i in self.run(domain):
            li.append(i)
        arr_subdomain = list(set(li))
        self.subdomain_num = len(arr_subdomain)
        for i in arr_subdomain:
            self.sub_file.write(i + '\n')
        self.sub_file.close()
        print('\033[034m[INFO]\033[0m Number of subdomains: %s' % self.subdomain_num)
        print('\033[032m[SUCC]\033[0m GetDomain Module Has Finished Running!')

    # -f参数
    def file_get_subdomain(self, file):
        arr_subdomain = []
        start_time = time.time()
        print('\033[034m[INFO]\033[0m GetDomain Module Running!')
        with open(file, 'r') as f:
            for domain in f.readlines():
                domain = domain.strip('\n')
                self.domain_q.put(domain)
        total_num = self.domain_q.qsize()
        print('\033[34m[INFO]\033[0m The total number of targets to be detected is: %d' % total_num)
        thread_list = []

        def thread_file(q, li, func):
            while not q.empty():
                d = q.get()
                end_time = time.time()
                program_time = (end_time - start_time)
                threading.Thread(target=self.file_get_progress, args=(total_num, program_time,)).start()
                for i in func(d):
                    li.append(i)

        for i in range(15):
            t = threading.Thread(target=thread_file, args=(self.domain_q, arr_subdomain, self.run))
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        # --- 域名去重
        arr_subdomain = list(set(arr_subdomain))
        self.subdomain_num = len(arr_subdomain)
        for i in arr_subdomain:
            self.sub_file.write(i + '\n')
        self.sub_file.close()
        print('\n\033[034m[INFO]\033[0m Number of subdomains: %s' % self.subdomain_num)
        print('\033[032m[SUCC]\033[0m GetDomain Module Has Finished Running!')

    # 进度条
    def file_get_progress(self, total_num, _time):
        """
        :param _time:
        :param total_num: 所有需要探测的域名数量
        :return:
        """
        get_num = total_num - self.domain_q.qsize()
        Remaining_time = (total_num * time / get_num) - _time  # 程序剩余运行时间 预计总时间-已运行时间
        print('\r\033[34m[PROG]\033[0m Detected: %d Progress: %.2f %% Time: %.2fs The Remaining time: %.2fs' % (
            get_num, (get_num / total_num * 100), _time, Remaining_time), end="")


if __name__ == '__main__':
    UseGetSubDomain().get_subdomain('baidu.com')
