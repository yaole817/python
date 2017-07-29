# -*- coding: utf-8 -*
import requests
import re
import sys,locale


htmlKeyWords = {
                "\\u003d":'=',
                "\\u0026":'&'

                }
#淘宝爬虫类
class TAOBAO:
    #初始化，传入基地址，页数
    def __init__(self,baseUrl,page,goods):
        self.goods=goods
        self.baseUrl=baseUrl+self.goods
        self.page=page
        self.defaultgoods=u"淘宝"
        self.ilt=[]        
        self.file=None
    #传入url，获取页面代码
    def getHTMLText(self,url):
        #headers={'user-agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"}
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",}
        try:
            r=requests.get(url,headers=headers,timeout=30)
            #r.encoding=r.apparent_encoding
            return r.text
        except:
            print("error")
        #except requests.exceptions.RequestException,e:
        #    print e
    #摘取所要数据    
    def parsePage(self,html):
        try:
            plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
            tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
            npl = re.findall(r'\"view_sales\"\:\"[\d]*',html)
            links = re.findall(r'detail_url\"\:\".*?\"',html)
            
            for i in range(len(plt)):
                price = eval(plt[i].split(':',1)[1])
                title = eval(tlt[i].split(':',1)[1])
                num   = eval(npl[i].split(':"',1)[1])
                if "http" in links[i]:
                    link  = links[i].split(':',1)[1].replace('"','')
                else:
                    link  = "https:"+links[i].split(':',1)[1].replace('"','')
                for key in htmlKeyWords:
                    link = link.replace(key,htmlKeyWords[key])
                self.ilt.append([price , num, title,link])
        except:
            print("摘取数据出错").encode('utf-8')
            return None
    #打印数据
    def printGoodsList(self):

        tplt = "{:^4}\t{:<14}\t{:<10}\t{:^80}"
        print (tplt.format("序号", "价格","成交量", "商品名称", ))
        count = 0
        for g in self.ilt:
            count = count + 1
            print(tplt.format(count, g[0], g[1], g[3],chr(32)))
    #创建存入数据文件
    def setFileTitle(self):

            self.file = open(goods + ".txt","w+")
    #写入数据    
    def writeData(self):
        tplt = "{:^4}\t{:<14}\t{:<10}\t{:^80}"
        self.file.write(tplt.format("序号", "价格","成交量", "商品链接", )+"\n")
        count = 0
        for g in self.ilt:
            count = count + 1
            self.file.write(tplt.format(count, g[0], g[1], g[3],chr(32))+"\n")

    def start(self):
        self.setFileTitle()
        for i in range(self.page):
            try:
                url = self.baseUrl + '&s=' + str(44*i)
                html = self.getHTMLText(url)
                self.parsePage(html)
            except:
                continue
        self.printGoodsList()
        self.writeData()

goods='机器学习'#input("Please input goods what you what:")
baseurl = "https://s.taobao.com/search?q="
page =int(input("Please input pages:"))
tb = TAOBAO(baseurl,page,goods)
tb.start()
