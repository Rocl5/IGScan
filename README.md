# IGScan(Infomation Gathering Scan)
## What can it do? 
>一、收集子域名，并将可访问的链接放入到result.txt中， 子域名放到subdomain.txt中
>二、端口扫描(正在实现)
>三、web容器指纹识(预期功能)
## How to use?
>探测单个域名 使用参数-u

```
Usage: python3 IGScan.py -u testphp.vulnweb.com
```
>探测多个域名
首先需要编辑一个targets.txt，写入需要探测的域名，使用参数-f指定文件

```
Usage: python3 IGScan.py -f targets.txt 
```
## Run screenshot
![image](https://github.com/ro4lsc/GTL/blob/master/screenshot.png)

## 法律声明
本工具仅能在取得足够合法授权的企业安全建设中使用，在使用本工具过程中，您应确保自己所有行为符合当地的法律法规。 如您在使用本工具的过程中存在任何非法行为，您将自行承担所有后果，本工具所有开发者和所有贡献者不承担任何法律及连带责任。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。 您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。

## 后续想法
首先肯定是完善成一个信息收集的工具，端口扫描，web容器指纹收集肯定是要有的
后续会与crawlergo+xray进行联动,有时间的话将会更新

大佬们给萌新点点star吧，跪～
