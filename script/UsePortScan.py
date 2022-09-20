from core.get_port import Masscan
from core.get_port import Nmapscan


class PortScan(object):

    def __init__(self):
        pass

    def nmapscan(self, hosts):
        nmapscan = Nmapscan(hosts)
        nmapscan.nmapscan()

    def masscan(self, hosts):
        masscan = Masscan(hosts)
        masscan.masscan()