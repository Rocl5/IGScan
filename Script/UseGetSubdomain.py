from Core.GetSubdomain import GetSubdomain


class GetDomain:

    def __init__(self, url, targets_filename):
        self.url = url
        self.arr_subdomain = []  # 去重后的域名
        self.targets_filename = targets_filename  # 放置域名的txt
        self.subdomain_filename = 'subdomain.txt'  # 子域名result
        self.GetSubdomain = GetSubdomain()

    def UseApi(self, arr_subdomain, url):
        GetSubdomain = self.GetSubdomain
        for i in GetSubdomain.ce_baidu(url):
            arr_subdomain.append(i + '\n')
        for i in GetSubdomain.hackertarget(url):
            arr_subdomain.append(i + '\n')
        for i in GetSubdomain.IP138(url):
            arr_subdomain.append(i + '\n')
        for i in GetSubdomain.crtsh(url):
            arr_subdomain.append(i + '\n')
        for i in GetSubdomain.qianxun(url):
            arr_subdomain.append(i + '\n')
        for i in GetSubdomain.aizhan(url):
            arr_subdomain.append(i + '\n')


    def url_Getdomain(self):
        print('\033[034m[INFO]\033[0m GetDomain Module Running!')
        open_subdomainfile = open(self.subdomain_filename, 'w')
        arr_subdomain = self.arr_subdomain
        url = self.url
        url = url.strip('\n')
        self.UseApi(self.arr_subdomain, url)
            # 自定义去重方法
        for i in range(len(arr_subdomain), 0, -1):
            for j in range(1, len(arr_subdomain)):  # 这个为0就把自己给删了，所以需要注意
                try:
                    if arr_subdomain[i] == arr_subdomain[i-j]:
                        del arr_subdomain[i]
                except:
                    pass
        for i in arr_subdomain:
            open_subdomainfile.write(i)
        open_subdomainfile.close()
        print('\033[032m[SUCC]\033[0m GetDomain Module Has Finished Running!')

    def file_Getdomain(self):
        # --定义header头
        print('\033[034m[INFO]\033[0m GetDomain Module Running!')
        open_subdomainfile = open(self.subdomain_filename, 'w')  # 写入subdomain.txt文件
        arr_subdomain = self.arr_subdomain
        with open(file=self.targets_filename, mode='r') as domain:
            for url in domain.readlines():
                print('\033[34m[INFO]\033[0m Retrieving: %s' % url, end="")
                url = url.strip('\n')
                self.UseApi(self.arr_subdomain, url)
                    # --- 域名去重
            for i in range(len(arr_subdomain), 0, -1):
                for j in range(1, len(arr_subdomain)):  # 这个为0就把自己给删了，所以需要注意
                    try:
                        if arr_subdomain[i] == arr_subdomain[i-j]:
                            del arr_subdomain[i]
                    except:
                        pass
            for i in arr_subdomain:
                open_subdomainfile.write(i)
        open_subdomainfile.close()
        print('\033[032m[SUCC]\033[0m GetDomain Module Has Finished Running!')
