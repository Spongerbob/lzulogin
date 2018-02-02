#-*- coding:UTF-8 -*-

import urllib.request
import urllib
import gzip
import http.cookiejar
import time

#定义一个方法用于生成请求头信息，处理cookie
def getOpener(head):
    # deal with the cookies
    #<pre name="code" class="python">
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

#定义一个方法来解压返回信息
def ungzip(data):
    try:      #尝试解压
        print('正在解压……')
        data = gzip.decompress((data))
        print('解压完毕！')
    except:
        print('未经压缩，无需解压')
    return data

#封装头信息，伪装成浏览器
header = {
    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    #'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
    'Accept': ' */*',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': '10.10.1.6',
}

url = 'http://10.10.1.6/include/auth_action.php'
opener = getOpener(header)

id = 'zhanghb2017'
password = 'zhb19961211'

postDict = {
    'action': 'login',
    'username': id,
    'password': password,
    'domain': '@cernet',
    'ac_id' : '1',
    'user_ip': '',
    'nas_ip': '',
    'user_mac': '',
    'save_me': '1',
    'ajax': '1',
}

while 1:
    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open(url, postData)
    data = op.read()
    data = ungzip(data)

    print(data)
    time.sleep(10)