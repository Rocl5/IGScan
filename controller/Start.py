from .controller import Subdomain, Checkurl, Portscan, Webanaylzer


class IGScan(object):
    def __init__(self, url, file, hosts, is_subdomain, is_checkurl, is_webanalyzer):
        self.url = url
        self.file = file
        self.hosts = hosts
        self.is_sub = is_subdomain
        self.is_check = is_checkurl
        self.is_web = is_webanalyzer
        self.Subdomain = Subdomain()
        self.Checkurl = Checkurl()
        self.PortScan = Portscan()
        self.Webanaylzer = Webanaylzer()

    def Start(self):
        # print(module)
        if self.is_sub is not None:
            if self.file is not None:
                self.Subdomain.file_subdomain(self.file)
            else:
                self.Subdomain.url_subdomain(self.url)
        if self.is_check is not None:
            if self.file is not None:
                self.Checkurl.file_Check(self.file)
            else:
                self.Checkurl.url_Check()

        # if module != '' and module != None:
        #     module = module.split(',')
        #     if url != '' and url != None:
        #         all_module = ['subdomain', 'checkurl', 'webanalyzer']
        #         inse_module = list(set(all_module).intersection(set(module)))  # 交集
        #         dif_module = list(set(all_module).difference(set(module)))  # 并集
        #         # print(module)
        #         if len(dif_module) == 0:
        #             starttime = time.time()
        #             Subdomain.url_subdomain(url)
        #             Checkurl.url_Check()
        #             Webanaylzer.url_analyzer()
        #             endtime = time.time()
        #             print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #             print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #
        #         if len(dif_module) == 1:
        #             if module[0] == 'subdomain':
        #                 starttime = time.time()
        #                 Subdomain.url_subdomain(url)
        #                 Checkurl.url_Check()
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #             if module[0] == 'webanalyzer':
        #                 starttime = time.time()
        #                 Subdomain.url_subdomain(url)
        #                 Checkurl.url_Check()
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #
        #         if len(inse_module) == 1:
        #             if module[0] == 'subdomain':
        #                 starttime = time.time()
        #                 Subdomain.url_subdomain(url)
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #             elif module[0] == 'checkurl':
        #                 starttime = time.time()
        #                 Checkurl.url_Check()
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #             elif module[0] == 'webanalyzer':
        #                 starttime = time.time()
        #                 Webanaylzer.one_analyzer(url)
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #
        #     if targets_file != '' and targets_file != None:
        #         all_module = ['subdomain', 'checkurl', 'webanalyzer']
        #         inse_module = list(set(all_module).intersection(set(module)))
        #         dif_module = list(set(all_module).difference(set(module)))
        #         # print(module)
        #         if len(dif_module) == 0:
        #             starttime = time.time()
        #             Subdomain.file_subdomain(targets_file)
        #             Checkurl.file_Check(targets_file)
        #             Webanaylzer.file_analyzer(targets_file)
        #             endtime = time.time()
        #             print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #             print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #
        #         if len(dif_module) == 1:
        #             if module[0] == 'subdomain':
        #                 starttime = time.time()
        #                 Subdomain.file_subdomain(targets_file)
        #                 Checkurl.file_Check(targets_file)
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #             if module[0] == 'webanalyzer':
        #                 starttime = time.time()
        #                 Subdomain.file_subdomain(targets_file)
        #                 Checkurl.file_Check(targets_file)
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #
        #         if len(inse_module) == 1:
        #             if module[0] == 'subdomain':
        #                 starttime = time.time()
        #                 Subdomain.file_subdomain(targets_file)
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #             elif module[0] == 'checkurl':
        #                 starttime = time.time()
        #                 Checkurl.file_Check(targets_file)
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
        #             elif module[0] == 'webanalyzer':
        #                 starttime = time.time()
        #                 Webanaylzer.file_analyzer(targets_file)
        #                 endtime = time.time()
        #                 print('\033[32m[SUCC]\033[0m All target links have been collected!')
        #                 print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

        if self.hosts != '' and self.hosts != None:
            if '/' in self.hosts:
                self.PortScan.masscan(self.hosts)
            else:
                self.PortScan.nmapscan(self.hosts)

if __name__ == '__main__':
    # IGScan()
    pass