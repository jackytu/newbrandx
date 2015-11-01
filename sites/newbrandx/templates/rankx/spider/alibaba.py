#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: jackytu<zhongying.tu@gmail.com>
import urllib.request
import re

def webmethod():
    from selenium import webdriver
    driver = webdriver.Plantomjs()
    driver.set_window_size(1024, 768)
    driver.get('http://detail.tmall.com/item.htm?id=37593658559')
    mystr=str(driver.page_source)
    driver.quit()
    return mystr

def getmethod(url):
    headers1 = {'GET': '',
                'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; Media Center PC 6.0; InfoPath.3; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)",
                }
    req=urllib.request.Request(url,headers=headers1)
    html = urllib.request.urlopen(req).read()
    #scode = str(html, "gbk").encode("utf8")
    #scode = urllib.request.urlopen(req).read()
    scode = html.decode("gbk","ignore")
    writeinfile('output.txt', scode)
    return scode
'''
def findallgoods(s):
    head='<p class="pic-box">\n                <a href="'
    tail='" target'
    n=re.findall(head+'(.*?)'+tail,s)
    return n
'''
def searchintaobao(keyword,price0=-1,price1=-1,sorttype=0,page=1):
    isfilter=0
    if price0!=-1:
        isfilter=1
        pricestr='[{0},]'.format(price0)
        pricestr='filter=reserve_price'+urllib.request.quote(pricestr,encoding='gbk')
    else:
        pricestr=''
    if price1!=-1:
        isfilter=1
        pricestr='[{0},{1}]'.format(price0,price1)
        pricestr='filter=reserve_price'+urllib.request.quote(pricestr,encoding='gbk')
    head='http://s.taobao.com/search?'
    sort={0:'default',1:'renqi-desc',2:'sale-desc',3:'credit-desc',4:'price-asc',5:'price-desc'}
    page=(page-1)*44
    pagestr='&s={0}'.format(page)
    sortstr='&sort='+sort[sorttype]
    keystr='&tab=all&q='+urllib.request.quote(keyword,encoding='gbk')
    url=head+pricestr+sortstr+keystr+pagestr
    print(url)
    return url

def getallgoods(keyword,price0=-1,price1=-1,sorttype=-1,page=4):
    m=[]
    for i in range(page-1):
        url=searchintaobao(keyword,price0,price1,sorttype,i+1)
        scode=getmethod(url)
        nid=taobaoID(scode)
        m+=nid
    return m

def num2utf8(num):
    uhex=hex(num)
    str1="u'\\u{0}'".format(uhex)
    str1=str1.replace('0x','')
    c=eval(str1)
    return c

def getinfo(itemid):
    headers_item={'GET': '',
                'Host': "item.taobao.com",
                'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2;\
WOW64; Trident/7.0; .NET4.0E; .NET4.0C; Media Center PC 6.0; InfoPath.3;\
.NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)"}
    open_url=r'http://detail.tmall.com/item.htm?spm=a230r.1.0.0.yquayA&id={0}'.format(itemid)
    item_req=urllib.request.Request(open_url,headers=headers_item)
    urlopen=urllib.request.urlopen(item_req)
    real_url=urlopen.geturl()
    print(real_url)
    scode=urlopen.read().decode('gbk', 'ignore')

    if real_url.find('taobao')==-1:
    #天猫
        headers_tmall={'GET': '',
                'Host': "ext.mdskip.taobao.com",
                'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2;\
WOW64; Trident/7.0; .NET4.0E; .NET4.0C; Media Center PC 6.0; InfoPath.3;\
.NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)",
                'Referer': real_url}
        #获取交易记录URL

        buyer_list=r'http://ext.mdskip.taobao.com/extension/dealRecords.htm?'
        try:
            buyer_url=buyer_list+re.search(buyer_list+'(.*?)" >',scode).group(1)
        except AttributeError:
            print('Cannot get tmall_buyerlist')
            buyer_url=''
        #获取当前价格
        current_p=r'http://mdskip.taobao.com/core/initItemDetail.htm?'
        try:
            current_price=current_p+re.search(current_p+'(.*?)"',scode).group(1)
            price_req=urllib.request.Request(current_price,headers=headers_tmall)
            price_scode=urllib.request.urlopen(price_req).read().decode('gbk', 'ignore')
            try:
                price=re.search(r'"extraPromPrice":"(\d{1,8}.\d{1,4})"',price_scode).group(1)
            except AttributeError:
                price=re.search(r'"price":"(\d{1,8}.\d{1,4})"',price_scode).group(1)
            price=float(price)
            #获取销量

            try:
                sells=re.search(r'"sellCount":(\d{1,12})',price_scode).group(1)
            except AttributeError:
                print('Cannot get Tmall Sell_count')
                sells=-1
        except AttributeError:
            print('Cannot get Tmall current price')
            price=-1

        #获取关键信息
        try:
            place=re.search(r'产地:&nbsp;(.*?)<',scode).group(1)
        except AttributeError:
            place=-1
        try:
            net=re.search(r'净含量:&nbsp;(.*?)<',scode).group(1)
        except AttributeError:
            net=-1
        try:
            brand=re.search('品牌:&nbsp;(.*?)<',scode).group(1)
        except AttributeError:
            brand=-1

        #对于葡萄酒的
        try:
            win_type=re.search(r'葡萄酒种类:&nbsp;(.*?)<',scode).group(1)
        except AttributeError:
            win_type=-1
        try:
            win_gout=re.search(r'口味:&nbsp;(.*?)<',scode).group(1)
        except AttributeError:
            win_gout=-1
        if place.find('&#')!=-1:
            #转码为utf8
            places=''
            for num in re.findall(r'&#(\d{5})',place):
                places+=num2utf8(int(num))
            place=places
            brands=''
            try:
                oldbrand=re.search('(^\w+$)',brand).group(1)
                brands+=oldbrand
            except AttributeError:
                pass
            for num in re.findall(r'&#(\d{5})',brand):
                brands+=num2utf8(int(num))
            brand=brands
            try:
                win_types=''
                for num in re.findall(r'&#(\d{5})',win_type):
                    win_types+=num2utf8(int(num))
                win_type=win_types
                win_gouts=''
                for num in re.findall(r'&#(\d{5})',win_gout):
                    win_gouts+=num2utf8(int(num))
                win_gout=win_gouts
            except TypeError:
                pass

        #读取若干页成交记录，获取价格分布
        if buyer_url=='':
            print('cannot open buyer list')
            pass
        else:
            price_re=[]
            quantity_re=[]
            price_dis={}
            re_scode=''
            for i in range(1,6):
                re_url=buyer_url.replace('bid_page=1&','bid_page={0}&'.format(i))
                re_req=urllib.request.Request(re_url,headers=headers_tmall)
                re_scode+=urllib.request.urlopen(re_req).read().decode('gbk', 'ignore')
            re_table=re.findall(r'<tr(.*?)</tr>',re_scode)
            if len(re_table)==0:
                print('Cannot get the buyer table\n')
            else:
                for t in re_table:
                    #print(t)
                    re_style=re.search(r'<td class=\\"cell-align-l style\\">(.*?)</td>',t).group(1)
                    try:
                        re_quantity=re.search(r'<td class=\"quantity\">(.*?)</td>',t).group(1)
                    except AttributeError:
                        re_quantity=re.search(r'<td class=\\"quantity\\">(.*?)</td>',t).group(1)
                    try:
                        re_price=re.search(r'td class=\\"price\\"><em>.*?(\d{1,10}.\d{1,5}).*?</em>.*?</td>',t).group(1)
                    except AttributeError:
                        try:
                            re_price=re.search(r'td class=\"price\"><em>.*?(\d{1,10}.\d{1,5}).*?</em>.*?</td>',t).group(1)
                        except AttributeError:
                            re_price=price
                    re_date=re.search(r'<td class=\\"dealtime\\"> <p class=\\"date\\">(.*?)</p>.*?</td>',t).group(1)
                    try:
                        price_re.append(float(re_price))
                        quantity_re.append(float(re_quantity))
                    except ValueError:
                        pass
            if len(price_re)!=0:
                re_n=sum(quantity_re)
                price_set=set(price_re)
                for p_r in price_set:
                    p_c=price_re.count(p_r)
                    total_p=0
                    p_index0=-1
                    for j in range(p_c):
                        try:
                            p_index0=price_re[p_index0+1:].index(p_r)
                            total_p+=quantity_re[p_index0]
                        except IndexError:
                            pass
                    price_dis[p_r]=p_r*total_p/re_n
        if price==-1:
            pass
        else:
            if win_type==-1 and win_gout==-1:
                #不是酒
                info=(itemid,price,sells,place,net,brand,price_dis)
            else:
                info=(itemid,price,sells,place,net,brand,win_type,win_gout,price_dis)
            return info
    else:
        #淘宝
        headers_taobao={'GET': '',
                'Host': "detailskip.taobao.com",
                'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2;\
WOW64; Trident/7.0; .NET4.0E; .NET4.0C; Media Center PC 6.0; InfoPath.3;\
.NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)",
                'Referer': real_url}
        #获取交易记录URL
        buyer_list=r'http://detailskip.taobao.com/json/show_buyer_list.htm'
        try:
            buyer_url=buyer_list+re.search(buyer_list+'(.*?)" >',scode).group(1)
        except AttributeError:
            print('Cannot get buyerlist')
            buyer_url=''
        #获取当前价格
        current_p=r'http://detailskip.taobao.com/json/sib.htm'
        try:
            current_price=current_p+re.search(current_p+'(.*?)"',scode).group(1)
        except AttributeError:
            print('Cannot get price_url')
        price_req=urllib.request.Request(current_price,headers=headers_taobao)
        price_scode=urllib.request.urlopen(price_req).read().decode('gbk', 'ignore')
        try:
            price=re.search(r'price:"(\d{1,8}.\d{1,4})"',price_scode).group(1)
            price=float(price)
        except AttributeError:

            print('Cannot get current price')
            print(current_price)
            print(price_scode)
            price=-1
        #获取销量
        sell_c=r'http://detailskip.taobao.com/json/ifq.htm?'
        try:
            sell_count=sell_c+re.search(sell_c+'(.*?)"',scode).group(1)
        except AttributeError:
            print('cannt get sell_count url')
        sell_req=urllib.request.Request(sell_count,headers=headers_taobao)
        sell_scode=urllib.request.urlopen(sell_req).read().decode('gbk', 'ignore')
        try:
            sells=re.search(r'confirmGoods: (\d{1,12}),',sell_scode).group(1)
        except AttributeError:
            print('Cannot get Sell_count')
            print(sell_scode)
            sells=-1
        #获取关键信息
        try:
            place=re.search(r'产地:(.*?)<',scode).group(1)
        except AttributeError:
            place=-1
        try:
            net=re.search(r'净含量:(.*?)<',scode).group(1)
        except AttributeError:
            net=-1
        try:
            brand=re.search('品牌:(.*?)<',scode).group(1)
        except AttributeError:
            brand=-1

        #对于葡萄酒的
        try:
            win_type=re.search(r'葡萄酒种类:(.*?)<',scode).group(1)
        except AttributeError:
            win_type=-1
        try:
            win_gout=re.search(r'口味:(.*?)<',scode).group(1)
        except AttributeError:
            win_gout=-1

        #读取若干页成交记录，获取价格分布
        if buyer_url=='':
            print('cannot open buyer list')
            pass
        else:
            price_re=[]
            quantity_re=[]
            price_dis={}
            re_scode=''
            for i in range(1,6):
                re_url=buyer_url.replace('bid_page=1&','bid_page={0}&'.format(i))
                re_req=urllib.request.Request(re_url,headers=headers_taobao)
                re_scode+=urllib.request.urlopen(re_req).read().decode('gbk', 'ignore')
            re_table=re.findall(r'<tr(.*?)</tr>',re_scode)
            if len(re_table)==0:
                print(buyer_url)
                print('Cannot get the buyer table\n')
            else:
                for t in re_table:
                    #print(t)
                    re_style=re.search(r'<td class=\\"cell-align-l style\\">(.*?)</td>',t).group(1)
                    try:
                        re_quantity=re.search(r'<td class=\"quantity\">(.*?)</td>',t).group(1)
                    except AttributeError:
                        re_quantity=re.search(r'<td class=\\"quantity\\">(.*?)</td>',t).group(1)
                    try:
                        re_price=re.search(r'td class=\\"price\\"><em>.*?(\d{1,10}.\d{1,5}).*?</em>.*?</td>',t).group(1)
                    except AttributeError:
                        try:
                            re_price=re.search(r'td class=\"price\"><em>.*?(\d{1,10}.\d{1,5}).*?</em>.*?</td>',t).group(1)
                        except AttributeError:
                            re_price=price
                    re_date=re.search(r'<td class=\\"dealtime\\"> <p class=\\"date\\">(.*?)</p>.*?</td>',t).group(1)
                    try:
                        price_re.append(float(re_price))
                        quantity_re.append(float(re_quantity))
                    except ValueError:
                        pass
            if len(price_re)!=0:
                re_n=sum(quantity_re)
                price_set=set(price_re)
                for p_r in price_set:
                    p_c=price_re.count(p_r)
                    total_p=0
                    p_index0=-1
                    for j in range(p_c):
                        try:
                            p_index0=price_re[p_index0+1:].index(p_r)
                            total_p+=quantity_re[p_index0]
                        except IndexError:
                            pass
                    price_dis[p_r]=p_r*total_p/re_n
        if price==-1:
            pass
        else:

            if win_type==-1 and win_gout==-1:
                #不是酒
                info=(itemid,price,sells,place,net,brand,price_dis)
            else:
                info=(itemid,price,sells,place,net,brand,win_type,win_gout,price_dis)
            return info


def taobaoID(s):
    restr='&sid='
    n=re.findall(r'&sid=(\d*?)&bid=(\d*?)&',s)
    #name=re.findall(r'',s)
    return n

def writeinfile(filename,s2write,mode='w',encoding='utf-8'):
    file=open(filename,mode=mode,encoding=encoding)
    file.write(s2write)
    file.close()



def mainfun(keyword,price0=-1,price1=-1,sorttype=-1,page=4):
    keyword=str(keyword)
    m=getallgoods(keyword,price0,price1,sorttype,page)

    print(m)

    info=[]
    mystr=''
    for nid in m:
        info=getinfo(nid[1])
        try:
            for i in range(len(info)):
                mystr=mystr+str(info[i])+'\t'
        except TypeError:
            pass
        mystr+='\n'
    writeinfile('sellcount.txt',mystr)
    return mystr

if __name__ == '__main__':
    mainfun('iphone6s', 0, 10000, 2, 4)
