import time

from script.UseCheckURL import CheckURL
from script.UseGetSubdomain import GetSubDomain
from script.UsePortScan import PortScan
from script.UseWebAnaylzer import Anaylzer


class Subdomain(object):
    def __init__(self):
        self.subdomain_file = 'output/subdomain.txt'

    def url_subdomain(self, url):
        GetSubDomain().get_subdomain(url)

    def file_subdomain(self, targets_filename):
        GetSubDomain().file_get_subdomain(targets_filename)


class Checkurl(object):
    def url_Check(self):  # 当两个模块一起使用的时候可以
        Checkurl = CheckURL()
        Checkurl.url_start()

    def file_Check(self, targets_file):
        Checkurl = CheckURL()
        Checkurl.file_start(targets_file)


class Portscan(object):
    def __init__(self):
        pass

    def nmapscan(self, hosts):
        starttime = time.time()
        nmapscan = PortScan()
        nmapscan.nmapscan(hosts)
        endtime = time.time()
        print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

    def masscan(self, hosts):
        starttime = time.time()
        masscan = PortScan()
        masscan.masscan(hosts)
        endtime = time.time()
        print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))


class Webanaylzer:
    def one_analyzer(self, target_url):
        w = Anaylzer()
        w.one_module_start(target_url)

    def url_analyzer(self):
        w = Anaylzer()
        w.url_start()

    def file_analyzer(self, targets_file):
        w = Anaylzer()
        w.file_start(targets_file)
