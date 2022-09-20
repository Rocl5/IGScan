import argparse

from controller.Start import IGScan

"""
@auther: Rocl5
@version: v0.3
@descript: GetSubdomain模块: 获取子域名
           CheckURL模块: 判断存活链接
           PortScan模块: 端口扫描
           Anaylzer模块: Web容器指纹扫描
@time: 2020-08-09
"""
version = '1.0'
author = 'Rocl5'
IGScan_banner = """
Welcome to IGScan!
Version:%s Author: %s
""" % (version, author)
# Usage: python3 cli.py -u testphp.vulnweb.com -m subdomain,checkurl,webanaylzer
#        python3 cli.py -f targets.txt -m subdomain,checkurl,webanaylzer
#        python3 cli.py -i 127.0.0.1

parser = argparse.ArgumentParser(description="IGScan (Information Gathering Scan)")
parser.add_argument('-d', '--domain', help='domain')
parser.add_argument('-f', '--file', help='Place files for all domain names')
parser.add_argument('-i', '--ip', help='192.168.2.1 or CIDR 192.168.2.0/24')
parser.add_argument('-s', '--subdomain', help='subdomain module', default=None)
parser.add_argument('-c', '--checkurl', help='checkurl module', default=None)
parser.add_argument('-w', '--webanalyzer', help='webanalyzer module', default=None)
args = parser.parse_args()  # 实例化

hosts = args.ip
domain = args.domain
file = args.file
is_subdomain = args.subdomain
is_checkurl = args.checkurl
is_webanalyzer = args.webanalyzer
print(IGScan_banner)

IGScan = IGScan(domain, file, hosts, is_subdomain, is_checkurl, is_webanalyzer)
IGScan.Start()

