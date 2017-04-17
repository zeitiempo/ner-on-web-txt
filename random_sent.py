# coding:utf-8 #

from random import choice
import urllib2
from bs4 import BeautifulSoup as bs
import time


def random_sent():
    #       1    2    3    4    5    6    7    8   9   10 
    c_num=[ "50","40","27","36","34","24","21","4","31","24",
            #genesis,exodus,leviticus,numbers,deuteronomy,
            #joshua,judges,ruth,1 samuel,2 samuel,
            "22","25","29","36","10","13","10","42","150","31",
            #1 kings,2 kings,1 chronicles,2 chronicles,ezra,
            #nehemiah,esther,job,psalms,proverbs,
            "12","8","66","52","5","48","12","14","3","9",
            #ecclesiastes,song of songs,isaiah,jeremiah,lamentations,
            #ezekiel,daniel,hosea,joel,amos,
            "1","4","7","3","3","3","2","14","4","28",
            #obadiah,jonah,micah,nahum,habakkuk,
            #zephaniah,haggai,zechariah,malachi|matthew,
            "16","24","21","28","16","16","13","6","6","4",
            #mark,luke,john,acts,romans,
            #1 corinthians,2 corinthians,galatians,ephesians,philippians,
            "4","5","3","6","4","3","1","13","5","5",
            #colossians,1 thessalonians,2 thessalonians,1 timothy,2 timothy,
            #titus,philemon,hebrews,james,1 peter,
            "3","5","1","1","1","22"
            #2 peter,1 john,2 john,3 john,jude,revelation
           ]

    b=choice(xrange(66)) # which is the result of genuine book number minus 1
    c=choice(xrange(int(c_num[b]))) # which is the result of genuine chapter number minus 1

    b=b+1
    c=c+1

    b_quote="0"*(2-len(str(b)))+str(b)
    c_quote="0"*(3-len(str(c)))+str(c)   

    url="http://www.godcom.net/hhb/B"+b_quote+"C"+c_quote+".htm"
    user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'  
    headers = { 'User-Agent' : user_agent }  
    maxTryNum=10  
    for tries in range(maxTryNum):  
        try:  
            req = urllib2.Request(url, headers = headers)   
            context=urllib2.urlopen(req).read()  
            break  
        except:  
            if tries <(maxTryNum-1):  
                continue  
            else:  
                logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
                break  

    soup=bs(context,"html.parser")
    result=soup.find("p").find_all("tr")
    if result:
        sent=choice(result).get_text().strip()
        while len(sent)==8 or len(sent)==4:
            sent=choice(result).get_text().strip()
        sent=sent.encode('raw_unicode_escape')
        if "\u" in sent:
            sent=unicode(sent,'unicode-escape')
        else:
            sent=sent.decode("GB2312")
        #sent=sent.encode("utf-8")
        return b_quote+":"+sent

for i in xrange(20):
    print random_sent()
    time.sleep(1)
