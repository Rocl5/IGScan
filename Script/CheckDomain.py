import requests
import threading
import queue
import time


"""
@descript: 用来判断GetSubDomain得到的子域名是否可以访问
"""


queue = queue.Queue()


class CheckDomain:


    def __init__(self):
        self.target_filename = 'subdomain.txt'  # 打开子域名txt，并判断每个链接是否可以访问
        self.result_file = 'result.txt'
        self.num = 0


    def http_get(self, i):
        headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 QIHU 360EE"

        }
        try:
            i = 'http://' + i
            res = requests.get(url=i.strip('\n'), headers=headers, timeout=2)
            # print(res.status_code)
            if res.status_code == 200:
                # print(i)
                queue.put(i.strip('\n'))  # 放进队列
                self.num += 1 
        except:
            pass


    def https_get(self, i):
        headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 QIHU 360EE"
        }
        try:
            i = 'https://' + i
            res = requests.get(url=i.strip('\n'), headers=headers, timeout=2)
            # print(res.status_code)
            if res.status_code == 200:
                # print(i)
                queue.put(i.strip('\n'))
                self.num += 1
        except:
            pass


    def start(self):
        print('\033[34m[INFO]\033[0m CheckDomain Module Running!')
        thread_list = []
        f = open(self.target_filename, 'r') 
        for i in f.readlines():
            # print(get_url)
            t1 = threading.Thread(target=self.http_get, args=(i, ))
            thread_list.append(t1)
            t2 = threading.Thread(target=self.https_get, args=(i, ))
            thread_list.append(t2)
        for t in thread_list:
            t.setDaemon(True)
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        x = open(self.result_file, 'w')
        while not queue.empty():
            write_data = queue.get()
            x.write(write_data+'\n')
        x.close()
        print('\033[032m[SUCC]\033[0m CheckDomain Module Has Finished Running!')
        print('\033[034m[INFO]\033[0m The number of links obtained is: %d' % self.num)