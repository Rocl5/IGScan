import os
import time
from Script.UseGetSubdomain import GetDomain
from Script.UsePortScan import PortScan
from Script.CheckDomain import CheckDomain



class Subdomain:
    def __init__(self, url, targets_file):
        self.url = url
        self.targets_file = targets_file


    def file_subdomain(self):
        if self.targets_file != '' and self.targets_file != None:
            # print(self.targets_file)
            if os.path.exists('subdomain.txt'):
                if os.path.getsize('subdomain.txt') > 0:
                    print(
                        '\033[031m[WARN]\033[0m Check \033[032msubdomain.txt\033[0m exists and it not \033[031mnull\033[0m!')
                    YorN_GetSubdomain = input(
                        '\033[34m[INFO]\033[0m Have You need to subdomain detect? [\033[032mY\033[0m/\033[031mN\033[0m] ')
                    if YorN_GetSubdomain == 'Y' or YorN_GetSubdomain == 'y':
                        starttime = time.time()
                        Getdomain = GetDomain(url='', targets_filename=self.targets_file)  # GetDomain模块
                        Getdomain.file_Getdomain()
                        Checkdomain = CheckDomain()  # CheckDomain模块
                        Checkdomain.start()
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                        exit()
                    else:
                        starttime = time.time()
                        Checkdomain = CheckDomain()
                        Checkdomain.start()
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                        exit()

            starttime = time.time()
            Getdomain = GetDomain(url='', targets_filename=self.targets_file)
            Getdomain.file_Getdomain()
            Checkdomain = CheckDomain()
            Checkdomain.start()
            endtime = time.time()

            print('\033[32m[SUCC]\033[0m All target links have been collected!')
            print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

    def url_subdomain(self):
        starttime = time.time()
        Getdomain = GetDomain(url=self.url, targets_filename='')
        Getdomain.url_Getdomain()
        Checkdomain = CheckDomain()
        Checkdomain.start()
        endtime = time.time()

        print('\033[32m[SUCC]\033[0m All target links have been collected!')
        print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))



class Portscan:
    def __init__(self, hosts):
        self.hosts = hosts

    def nmapscan(self):
        starttime = time.time()
        nmapscan = PortScan(self.hosts)
        nmapscan.nmapscan()
        endtime = time.time()
        print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

    def masscan(self):
        starttime = time.time()
        masscan = PortScan(self.hosts)
        masscan.masscan()
        endtime = time.time()
        print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))