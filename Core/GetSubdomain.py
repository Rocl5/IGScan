import requests
import json
import re
import math
"""
@descript: 目前程序调用了六个接口用于获取子域名，后续会持续添加
@time: 2020-07-15
"""

class GetSubdomain:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }

    # 百度云观测
    def ce_baidu(self, domain):
        headers = self.headers
        subdomain_list = []
        url = 'http://ce.baidu.com/index/getRelatedSites?site_address={0}'.format(domain)
        res = re.findall(r'\.\w*', domain)  # 结果
        """
        思路就是从输入的域名在网页的内容中进行匹配[a-z0-9].baidu.com,最后将结果进行匹配
        """
        if len(res) == 3:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.') + res[2]
            except:
                temp_url = domain
        else:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.')  # 如果url为www.roalsc.top的话 匹配出['.ro4lsc', '.top']
                # print(temp_url)
            except:
                temp_url = domain  # 如果为roalsc.top则正常输出
        respon = requests.get(url, headers=headers)  # 访问这个接口，加个请求头防止被ban
        try:
            respon = json.loads(respon.text)  # 将json转换为字典
            for i in range(0, len(respon['data'])):  # 判断data里的数据长度，然后进行循环输出
            # 迭代器 迭代输出
            # 数据类型为json {"code":0,"data":[{"domain":"2013.sure56.com","score":80}
                # print(respon['data'][i]['domain'])  # 整了一堆废话，还是对json不了解的原因
                subdomain_list.append(respon['data'][i]['domain'])
        except:
            subdomain_list = []
        return subdomain_list


    # 爱站
    def aizhan(self, domain):

        subdomain_list = []
        url = 'https://baidurank.aizhan.com/baidu/{0}/'.format(domain)
        headers = self.headers
        respon = requests.get(url, headers=headers)  # 网页响应
        res = re.findall(r'\.\w*', domain)  # 结果
        """
        思路就是从输入的域名在网页的内容中进行匹配[a-z0-9].baidu.com,最后将结果进行匹配
        """
        if len(res) == 3:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.') + res[2]
            except:
                temp_url = domain
        else:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.')  # 如果url为www.roalsc.top的话 匹配出['.ro4lsc', '.top']
                # print(temp_url)
            except:
                temp_url = domain  # 如果为roalsc.top则正常输出
        res = re.findall(r'[a-z.0-9]*\.' + temp_url, respon.text)
        res = list(set(res))  # 去重
        for i in range(0,len(res)):  # 循环输出res列表中的值
            subdomain_list.append(res[i])
        return subdomain_list


    # hackertarget
    def hackertarget(self, domain):
        subdomain_list = []
        headers = self.headers
        res = re.findall(r'\.\w*', domain)  # 结果
        """
        思路就是从输入的域名在网页的内容中进行匹配[a-z0-9].baidu.com,最后将结果进行匹配
        """
        if len(res) == 3:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.') + res[2]
            except:
                temp_url = domain
        else:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.')  # 如果url为www.roalsc.top的话 匹配出['.ro4lsc', '.top']
                # print(temp_url)
            except:
                temp_url = domain  # 如果为roalsc.top则正常输出
        url = 'https://api.hackertarget.com/hostsearch/?q={0}'.format(temp_url)
        try:
            respon = requests.get(url, headers=headers)  # 网页响应
            res = re.findall(r'[a-z.0-9]*\.' + temp_url, respon.text)
            # print(res)
            for i in range(0, len(res)):
                subdomain_list.append(res[i])
        except:
            subdomain_list = []
        return subdomain_list


    # IP138
    def IP138(self, domain):
        subdomain_list = []
        url = 'https://site.ip138.com/{0}/domain.htm'.format(domain)
        headers = self.headers
        respon = requests.get(url, headers=headers)  # 网页响应
        res = re.findall(r'\.\w*', domain)  # 结果
        """
        思路就是从输入的域名在网页的内容中进行匹配[a-z0-9].baidu.com,最后将结果进行匹配
        """
        if len(res) == 3:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.') + res[2]
            except:
                temp_url = domain
        else:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.')  # 如果url为www.roalsc.top的话 匹配出['.ro4lsc', '.top']
                # print(temp_url)
            except:
                temp_url = domain  # 如果为roalsc.top则正常输出
        res = re.findall(r'[a-z.0-9]*\.' + temp_url, respon.text)
        res = list(set(res))  # 去重
        for i in range(0, len(res)):
            subdomain_list.append(res[i])
        return subdomain_list


    # crt.sh SSL 证书反查
    def crtsh(self, domain):
        subdomain_list = []
        url = 'https://crt.sh/?q=%25.{0}'.format(domain)
        headers = self.headers
        respon = requests.get(url, headers=headers)  # 网页响应
        res = re.findall(r'\.\w*', domain)  # 结果
        """
        思路就是从输入的域名在网页的内容中进行匹配[a-z0-9].baidu.com,最后将结果进行匹配
        """
        if len(res) == 3:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.') + res[2]
            except:
                temp_url = domain
        else:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.')  # 如果url为www.roalsc.top的话 匹配出['.ro4lsc', '.top']
                # print(temp_url)
            except:
                temp_url = domain  # 如果为roalsc.top则正常输出
        res = re.findall(r'[a-z.0-9]*\.' + temp_url, respon.text)
        res = list(set(res))  # 去重
        for i in range(0, len(res)):
            subdomain_list.append(res[i].lstrip('.'))
        return subdomain_list


    def qianxun(self, domain):
        """
        :param domain:
        :return:
        ;describe:首先访问页面获取页面中的查询结果数/20得到页面数，然后重新访问页面，使用循环遍历获取子域名
        """
        subdomain_list = []
        url = 'https://www.dnsscan.cn/dns.html'
        data = {
            "ecmsfrom": '8.8.8.8',
            "show": 'none',
            "keywords": domain
        }
        headers = self.headers
        res = re.findall(r'\.\w*', domain)  # 结果
        if len(res) == 3:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.') + res[2]
            except:
                temp_url = domain
        else:
            try:
                temp_url = res[0].strip('.') + '.' + res[1].strip('.')  # 如果url为www.roalsc.top的话 匹配出['.ro4lsc', '.top']
                # print(temp_url)
            except:
                temp_url = domain  # 如果为roalsc.top则正常输出
        respon = requests.post(url, headers=headers, data=data)
        try:
            result = re.findall(r'查询结果为:[0-9].*条', respon.text)  # 查询结果数，用来判断有多少页面，一个页面有20条数据
            result = re.findall(r'[0-9].*', result[0])
            result = result[0].strip('条')  # 查询的总数

            pagenum = int(result) / 20
            pagenum = math.ceil(pagenum)  # 这个math.ceil可以向上去整数，这个pagenum作为访问页面的页面数
            # 重新定义，重新访问
            for i in range(1, pagenum + 1):
                url = 'https://www.dnsscan.cn/dns.html?keywords={0}&page={1}'.format(domain, i)
                data = {
                    "ecmsfrom": '8.8.8.8',
                    "show": 'none',
                    "keywords": domain
                }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                }
                respon = requests.post(url, headers=headers, data=data)
                res = re.findall(r'[a-z.0-9]*\.' + temp_url, respon.text)
                res = list(set(res))  # 去重
                for i in range(0, len(res)):
                    subdomain_list.append(res[i])
        except:
            pass
        return subdomain_list
