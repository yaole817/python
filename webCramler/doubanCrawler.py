#!/usr/bin/python
#-*-coding:utf-8 -*-
import requests,re
import time
from bs4 import BeautifulSoup       
psudoWebHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def getAllUrl(url,helf,patten):
    #[helf+tag.get_text() for tag in tags]
    result = []
    wbData=requests.get(url,headers=psudoWebHeader)    #请求网址
    soup=BeautifulSoup(wbData.text,"lxml")  #解析网页信息
    #根据CSS路径查找标签信息，CSS路径获取方法，右键-检查-copy selector，tags返回的是一个列表
    tags=soup.select(patten)
    for tag in tags:
        tag=tag.get_text()    #将列表中的每一个标签信息提取出来
        url=helf+tag
        result.append(url)
    return result
        #print(url)    #网址组装完毕，输出

titlePat = re.compile(r'(?<=title=").*?(?=")')
authorPat = re.compile(r'(?<=class="pub">).*?(?=<)',re.DOTALL)
urlPat = re.compile(r'(?<=href=").*?(?=" onclick=&#34)')
imgPat = re.compile(r'(?<=src=").*?(?=" width="64" />)')
ratePat = re.compile(r'(?<="rating_nums">).*?(?=<)')
numberPat= re.compile(r'(?<=class="pl">).*?(?=<)',re.DOTALL)


tagPattern = "#content > div > div.article > div > div > table > tbody > tr > td > a" #all tags
#nexPage = '#subject_list > div.paginator > span.next > link'
def getNextPageUrl(wb_data,href):
    
    soup=BeautifulSoup(wb_data.text,"lxml") 
    for item in soup.find_all('link'):
        if 'next' in str(item):
            return href+item['href']
    return False

def decodeOnePage(wb_data):
    data0  = wb_data.content
    titles = titlePat.findall(data0)
    authors = [item.replace('\n','').replace(' ','') for item in authorPat.findall(data0)]
    rates = ratePat.findall(data0)
    numberOfPeople=[item.replace('\n','').replace(' ','') for item in numberPat.findall(data0)]
    return titles,rates,numberOfPeople,authors
    
def main():
    myUrl="https://book.douban.com/tag/?icn=index-nav"
    helf="https://book.douban.com/tag/" #观察一下豆瓣的网址，基本都是这部分加上标签信息，所以我们要组装网址，用于爬取标签详情页
    allTagUrls = getAllUrl(myUrl,helf,tagPattern) #find all tag urls 

    #data0 =getPageData(allUrls[0])
    for i in range(len(allTagUrls)): # list all tag urls
        myurl=allTagUrls[i]   # assign the tag url to value
        print(myurl)
        wb_data = requests.get(myurl,headers=psudoWebHeader)
        #titles,rates,numberOfPeople,authors=decodeOnePage(wb_data)
        #print(numberOfPeople[0].decode('utf-8'))
        #exit()
        try:
            wb_data = requests.get(myurl,headers=psudoWebHeader)
            name = myurl.replace(helf,'').encode('utf-8')
            #print(name.decode('utf-8'))
            with open('doubanBook\\'+name.decode('utf-8')+'.txt','wb+')as f:
                while True:
                    titles,rates,numberOfPeople,authors=decodeOnePage(wb_data)
                    num = min(len(titles),len(authors),len(rates))
                    for i in range(num):
                        f.write(titles[i]+','+rates[i]+','+numberOfPeople[i]+','+authors[i]+'\n')
                    if getNextPageUrl(wb_data,helf[:-5]):
                        nexPageUrl = getNextPageUrl(wb_data,helf[:-5]) #exact the next page url
                        myurl=nexPageUrl # get nex page url 
                        time.sleep(3)
                        print(nexPageUrl)
                        wb_data = requests.get(myurl,headers=psudoWebHeader)
                    else:break      
        except:
            print('tag continue')
            continue

if __name__ == '__main__':
    main()