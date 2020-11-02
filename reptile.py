#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
reptile.py
@note:Get movie reviews on Douban website
@auth:Grand li
@date:0:16 2020/10/31
'''


import requests         #网页请求模块
from lxml import etree  #网页请求数据解析模块


'''
获取浏览器header，获取方法参考：文档：（HTML小白）如何查看浏览器header.not...
链接：http://note.youdao.com/noteshare?id=70670aecae7e93819d249ed64ec3bb6f&sub=9C18A4AEA3A94BDD957B3454AFFE5321
'''
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

url = 'https://movie.douban.com/subject/1292600/'

'''
requests模块获取网页信息，获取方法参考：文档：Requests库.note
链接：http://note.youdao.com/noteshare?id=92255975cb542ac5bde15d974d237347&sub=95A577BFB210498794FEE452E0082C81
'''
r = requests.get(url,headers = headers)
print("status code:",r.status_code)
print(r.text)

html = etree.HTML(r.text)
result = etree.tostring(html)
print(result.decode('utf-8'))

'''
文档：xpath库解析.note
链接：http://note.youdao.com/noteshare?id=b015f44f747097f763ea2d5e0a6c36c9&sub=A88AB93624E942EA8630BE31A1384E65
'''
name = html.xpath('//*[@id="content"]/h1/span[1]/text()')
print(name)

point = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(point)

contect = html.xpath('//*[@id="link-report"]/span/text()/text()')
print(contect)








