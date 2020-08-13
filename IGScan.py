import argparse
from Controller.Controller import Subdomain, Portscan



"""
@auther: ro4lsc 
@version: v0.2
@descript: 配合Getsubdomain模块，达到收集域名的效果，并且将访问有效的链接放到result.txt里面
@time: 2020-08-09
"""


parser = argparse.ArgumentParser(description="IGScan (Information Gathering Scan)")
parser.add_argument('-u', '--url', help='Taget URL')
parser.add_argument('-f', '--file', help='Place files for all domain names')
parser.add_argument('-i', '--ip', help='192.168.2.1 or CIDR 192.168.2.0/24')

args = parser.parse_args()  # 实例化
targets_file = args.file
hosts = args.ip
url = args.url

if url != '' and url != None:
    Subdomain = Subdomain(url=url, targets_file='')
    Subdomain.url_subdomain()

if targets_file != '' and targets_file != None:
    Subdomain = Subdomain(url='', targets_file=targets_file)
    Subdomain.file_subdomain()

if hosts != '' and hosts != None:
    Portscan = Portscan(hosts)
    if '/' in hosts:
        Portscan.masscan()
    else:
        Portscan.nmapscan()

