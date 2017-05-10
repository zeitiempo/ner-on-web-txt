# coding:utf-8 #

import jieba
import codecs
import sys
import os
from random import choice
import urllib2
from bs4 import BeautifulSoup as bs
import re

def random_sent():
    sent="欢迎使用集成自然语言处理环境！本站提供了一些针对语料的集成自然语言处理环境，包括预处理、分词、专名识别，并有部分处理任务的实验性能展示。"
    '''
    #       1    2    3    4    5    6    7    8    9    10 
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
        sent=re.sub(r'([\d]+)','',sent)
        sent=sent[1:]
    '''
    
    return sent

def mm_tokenize(input_context):
        path=sys.path[0].replace(r"\\",r"/")
	vocab_in=codecs.open(path+"/INLPE/static/dic/vocab.txt","r","utf-8")
	vocab=vocab_in.readlines()
	tokenize=[]
	while input_context:
		i=min(5,len(input_context))
		word=input_context[:i]
		while len(word)!=1:
			if word+"\n" in vocab:
				tokenize.append(word)
				break
			else:
				word=word[:-1]
		if len(word)==1:
			tokenize.append(word)
		input_context=input_context[len(word):]
	
	return "/ ".join(tokenize).encode("utf-8")

def rmm_tokenize(input_context):
	path=sys.path[0].replace(r"\\",r"/")
        vocab_in=codecs.open(path+"/INLPE/static/dic/vocab.txt","r","utf-8")
	vocab=vocab_in.readlines()
	tokenize=[]
	while input_context:
		i=min(5,len(input_context))
		word=input_context[-i:]
		while len(word)!=1:
			if word+"\n" in vocab:
				tokenize.append(word)
				break
			else:
				word=word[1:]
		if len(word)==1:
			tokenize.append(word)
		input_context=input_context[:-len(word)]
	tokenize.reverse()
	
	return "/ ".join(tokenize).encode("utf-8")

def jieba_tokenize(input_context):
	tokenize_list=jieba.cut(input_context,cut_all=False)
	return "/ ".join(tokenize_list)

def mecab_tokenize(input_context):
    cmd=os.popen("echo "+input_context.encode("utf-8")+r" | mecab -d ./INLPE/static/mecab_chinese_data_binary_v0.3 -O wakati | sed 's/[[:space:]]/\/ /g'")
    return cmd.read()
