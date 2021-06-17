import os
from bs4 import BeautifulSoup
from pprint import pprint
import urllib.request as req
import sys

def naver():
    url ="https://weather.naver.com/"
    res= req.urlopen(url)
    soup=BeautifulSoup(res,"html.parser", from_encoding='euc-kr')

    
    cr_temp = soup.select('strong.current')
    cr_weather = soup.select('p.summary')
    cr_weather2 =soup.select('dl.summary_list')
    cr_lowset = soup.select('span.data.lowest')
    cr_highset = soup.select('span.data.highest')

    tempStr=str(cr_temp)    
    temp_1 = tempStr.replace('[<strong class="current">','')
    temp_2 = temp_1.replace('<span class="blind">현재 온도</span>','')
    temp = temp_2.replace('<span class="degree">°</span></strong>]','')

    lowsetStr=str(cr_lowset)
    lowset_1 = lowsetStr.replace('[<span class="data lowest">','')
    lowset_2 = lowset_1.replace('<span class="blind">평균기온</span>','')
    lowset = lowset_2.replace('<span class="degree">°</span></span>]','')

    highsetStr=str(cr_highset)
    highset_1 = highsetStr.replace('[<span class="data highest">','')
    highset_2 = highset_1.replace('<span class="blind">평균기온</span>','')
    highset = highset_2.replace('<span class="degree">°</span></span>]','')

    i=0
    tags=[]
    try: 
        tags.append(temp)
        tags.append(cr_weather[i].text)
        tags.append(cr_weather2[i].text)
        tags.append(lowset)
        tags.append(highset)        


        keywords = [tag for tag in tags]

        i += 1
    except IndexError:
        pass
    return keywords