import math
import queue
import re
import threading
import time

import requests
import requests.packages.urllib3

from utils.util import get_random_headers, fix_illegal_domain

requests.packages.urllib3.disable_warnings()
"""
@descript: 目前程序调用了六个接口用于获取子域名，后续会持续添加
"""

CE_BAIDU = "http://ce.baidu.com/index/getRelatedSites?site_address={}"
# AI_ZHAN = "https://baidurank.aizhan.com/baidu/{}/"
HACKER_TARGET = "https://api.hackertarget.com/hostsearch/?q={}"
IP138 = "https://site.ip138.com/{}/domain.htm"
CRTSH = "https://crt.sh/?q=%25.{}"


class GetSub(object):
    def __init__(self):
        self.headers = {"User-Agent": get_random_headers()}
        self.queue = queue.Queue()
        self.domain = None

    def req(self, url, api_name):
        try:
            res = requests.get(url.format(self.domain), headers=self.headers, timeout=15, verify=False)
            regexp = r"(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.){0,}" + self.domain.replace(
                ".", r"\."
            )
            res = re.findall(regexp, res.text)
            # print(len(res))
            for d in res:
                self.queue.put(d)
        except Exception as e:
            print('\n\033[031m[ERRO]\033[0m %s API ERROR!' % (api_name, ))

    def qianxun(self):
        """
        :param
        :return:
        ;describe:首先访问页面获取页面中的查询结果数/20得到页面数，然后重新访问页面，使用循环遍历获取子域名
        """
        url = 'https://www.dnsscan.cn/dns.html'
        data = {
            "ecmsfrom": '8.8.8.8',
            "show": 'none',
            "keywords": self.domain
        }
        resp = requests.post(url, headers=self.headers, data=data, verify=False)
        try:
            result = re.findall(r'查询结果为:[0-9].*条', resp.text)  # 查询结果数，用来判断有多少页面，一个页面有20条数据
            result = re.findall(r'[0-9].*', result[0])
            result = result[0].strip('条')  # 查询的总数
            page_num = int(result) / 20
            page_num = math.ceil(page_num)  # 这个math.ceil可以向上去整数，这个pagenum作为访问页面的页面数
            # 重新定义，重新访问
            thread_list = []
            for i in range(1, page_num + 1):  # 有多少page就创建多少个线程
                t = threading.Thread(target=self.qianxun_speed, args=(i, self.domain, self.headers,))
                thread_list.append(t)
            for t in thread_list:
                time.sleep(0.01)
                t.start()
            for t in thread_list:
                t.join()

                # for i in range(0, len(res)):
                #     queue.put(res[i])
        except:
            pass

    def qianxun_speed(self, page_num, domain, headers):
        url = 'http://www.dnsscan.cn/dns.html?keywords={0}&page={1}'.format(domain, page_num)
        data = {
            "ecmsfrom": '8.8.8.8',
            "show": 'none',
            "keywords": domain
        }
        respon = requests.post(url, headers=headers, data=data, verify=False)
        res = re.findall(r'[a-z.0-9]*\.' + domain, respon.text)
        for i in range(0, len(res)):
            self.queue.put(res[i])

    def run(self, domain):
        # 使用守护进程，调用每个函数，优化执行速度
        self.domain = fix_illegal_domain(domain)
        subdomain_list = []
        thread_list = []
        api_list = [CE_BAIDU, HACKER_TARGET, IP138, CRTSH]
        for api in api_list:
            thread_list.append(threading.Thread(target=self.req, args=(api, '')))
            # thread_list.append(threading.Thread(target=self.qianxun))
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()
        while not self.queue.empty():
            subdomain_list.append(self.queue.get())
        subdomain_list = list(set(subdomain_list))
        return subdomain_list


if __name__ == '__main__':
    li = GetSub().run('baidu.com')
    print(li)
    print(len(li))
