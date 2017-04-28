# coding:utf-8 #

import re
import codecs
import sys
import os 

def preprocess(f_i,f_o,parameter,label):
    fi=codecs.open(f_i,"r","utf-8")
    fo=codecs.open(f_o,"w","utf-8")
    context=fi.readlines()
    if parameter=="1":
        for line in context:
            result=line.split()
            line_len=len(result)
            fo.write(line_len+"\t")
            i=0
            for token in result:
                pair=re.match("(.*?)/(.*)",token)
                if pair:
                    word=pair.group(1).replace("[","").replace(" ","")
                    pos=pair.group(2)
                    pos_modify=re.match("(.*)\].*",pos)
                    if pos_modify:
                        pos=pos_modify.group(1)
                    if pos.startswith(label):
                        fo.write(str(i)+"\t")
                i=i+1
            fo.write("\n")
    else:
        for line in context:
            result=line.split()
            for token in result:
                pair=re.match("(.*?)/(.*)",token)
                if pair:
                    word=pair.group(1).replace("[","").replace(" ","")
                    pos=pair.group(2)
                    pos_modify=re.match("(.*)\].*",pos)
                    if pos_modify:
                        pos=pos_modify.group(1)
                    fo.write(word+"\t"+pos+"\n")
            fo.write("\n")
    fo.close()
    fi.close()

if __name__=='__main__':
    program=os.path.basename(sys.argv[0])
    f_i,f_o,parameter,label=sys.argv[1:5]
    preprocess(f_i,f_o,parameter,label)
