# IGScan(Infomation Gathering Scan)
## What can it do? 
一、收集子域名
<br/>
二、端口扫描(直接输出)
<br/>
三、web指纹识别

## How to use?
### Need
python3.6+
<br>

首先安装依赖
```
pip3 install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/
```
### 一、子域名探测
- 探测单个域名 使用参数-u
结果将会保存到`output/subdomain.txt`

Usage:
```
python3 cli.py -d example.com -s 1
```
- 探测多个域名
首先需要编辑一个targets.txt，写入需要探测的域名，使用参数-f指定文件

Usage: 
```
python3 cli.py -f targets.txt -s 1
```
### 二、判断指定域名是否存活
>如果是只单用这个模块的话，需要指定一个文本
故没有-u参数，毕竟没必要对一个url进行存活探测
但若是使用，是默认对output/subdomain.txt中的文本进行探测
结果将会保存到`output/link.txt`

Usage: 
```
python3 cli.py -f targets.txt -c 1 
```

### 三、web指纹识别
- 对单个url进行探测` (http://|https://)testphp.vulnweb.com`
```
python3 cli.py -d http://testphp.vulnweb.com -w 1
```
- 对某个文本中的url进行指纹识别
注意这里的url需要` (http://|https://)testphp.vulnweb.com`
```
python3 cli.py -f targets.txt -w 1 
```
### 四、组合使用
将子域名结果保存到
`output/subdomain.txt`
存活url保存到
`output/link.txt`
web指纹收集保存到
`output/fingerprint.txt`
- 单个url
```
python3 cli.py -d example.com -s 1 -c 1 -w 1
```
- 对某个文本中的url进行探测
```
python3 cli.py -f targets.txt -s 1 -c 1 -w 1
```

### 五、端口扫描

>使用参数 -i 指定ip

Usage:
```
python3 cli.py -i 192.168.2.1
python3 cli.py -i 192.168.2.0/24
```


## Run screenshot
![image](https://github.com/ro4lsc/IGScan/blob/master/Image/screenshot-1.png)
![image](https://github.com/ro4lsc/IGScan/blob/master/Image/screenshot-2.png)
![image](https://github.com/ro4lsc/IGScan/blob/master/Image/screenshot-3.png)
![image](https://github.com/ro4lsc/IGScan/blob/master/Image/screenshot-4.png)

## 法律声明
本工具仅能在取得足够合法授权的企业安全建设中使用，在使用本工具过程中，您应确保自己所有行为符合当地的法律法规。 如您在使用本工具的过程中存在任何非法行为，您将自行承担所有后果，本工具所有开发者和所有贡献者不承担任何法律及连带责任。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。 您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
