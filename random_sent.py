# coding:utf-8 #

from random import choice
import urllib2
from bs4 import BeautifulSoup as bs
import re
import chardet

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
response=urllib2.urlopen(url)
context=response.read()
soup=bs(context,"html.parser")
title=soup.find("h2").get_text().replace(" ","")
pattern=re.compile(r'\w*',re.L)
result=soup.find("p").find_all("tr")
if result:
    sent=choice(result).get_text().strip()
    if chardet.detect(sent.encode('raw_unicode_escape'))["encoding"] is "GB2312":
        sent=sent.encode('raw_unicode_escape')
    while len(sent)==4:
        sent=choice(result).get_text().strip()
    #print title
    print str(b)+":"+sent
