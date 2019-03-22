#!/usr/bin/env/ python
# coding=utf-8
import urllib2
from bs4 import BeautifulSoup
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def loaderequest(number, items):
    headers = {'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 59.0.3071.86 Safari / 537.36'}
#   request = urllib2.Request('https://hr.tencent.com/position.php?&start='+str(number), headers=headers)
    request = urllib2.Request('https://hr.tencent.com/position_detail.php?start=?'+str(number), headers=headers)
    html = urllib2.urlopen(request).read()
    a(html, items)
#    print html


def a(html, items):
    soup = BeautifulSoup(html, 'lxml')
    c = soup.select('.c')
    b = c
    for item in b:
        #   字典 键值对存储
        _item = {}
        _item['gangweizhize'] = item.select('td ').get_text()
        #  将提取出来的信息放入列表中
        items.append(_item)  


if __name__ == '__main__':

    number = 0
    items = []
    # 开关
    switch = True
    while switch:
        if number >= 50:
            switch = False
        loaderequest(number, items)
        number += 10
    content = json.dumps(items, ensure_ascii=False)
    with open('test.json', 'w')as f:
        f.write(content)