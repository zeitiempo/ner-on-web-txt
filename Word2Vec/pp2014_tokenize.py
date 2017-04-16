# coding:utf-8 #

import re
import codecs

fin=codecs.open("pp2014.txt","r","utf-8")
fout=codecs.open("pp2014_tokenize.txt","w","utf-8")
context=fin.readlines()
for line in context:
    result=line.split()
    for each in result:
        if each.endswith("/w"):
            pass
        else:
            pair=re.match("(.*?)/(.*)",each)
            if pair:
                token=pair.group(1).replace("[","")
                fout.write(token+"\t")
    fout.write("\n")
fout.close()
fin.close()
        
