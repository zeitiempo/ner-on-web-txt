# coding:utf-8 #

import codecs
import hashlib
import sys
import os

def crf_ner(input_context):
    path=sys.path[0]
    begin=0
    strlen=len(input_context)
    end=len(input_context)-1
    temp_name="tiny.txt"
    path_temp=path+"/static/crf_ner/"+temp_name
    temp=codecs.open(path_temp,"w","utf-8")
    for i in xrange(strlen):
        line=""
        left=max(begin,i-2)
        right=min(i+2,end)
        for a in xrange(left,right+1):
            line=line+"char["+str(a-i)+"]="+input_context[a]+"\t"
        if strlen>1:
            for b in xrange(left,right):
                line=line+"char["+str(b-i)+"]|char["+str(b-i+1)+"]="+input_context[b]+"|"+input_context[b+1]+"\t"
        if strlen>2:
            for c in xrange(left,right-1):
                line=line+"char["+str(c-i)+"]|char["+str(c-i+1)+"]|char["+str(c-i+2)+"]="+input_context[c]+"|"+input_context[c+1]+"|"+input_context[c+2]+"\t"
        if i==begin:
            line=line+"__BOS__\n"
        elif i==end:
            line=line+"__EOS__\n"
        else:
            line=line.strip()+"\n"
        temp.write(line)
    temp.close()
    path=sys.path[0].replace(r"\\",r"/")
    cmd=os.popen("crfsuite tag -m ./static/crf_ner/char3.model "+path_temp)
    ner=cmd.read()
    os.popen("rm "+path_temp).read()
    ner_list=ner.split("\n")
    loc=0
    result=""
    for each in ner_list[0:-2]:
        result=result+input_context[loc]+"/"+ner_list[loc]+" "
        loc=loc+1
    return result