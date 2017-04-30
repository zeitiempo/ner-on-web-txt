# coding:utf-8 #

import re
import codecs
import sys
import os

def mode1(f_i,label):
    fi=codecs.open(f_i,"r","utf-8")
    f_o_prefix=os.path.splitext(f_i)
    f_o=f_o_prefix+r"_loc.txt"
    fo=codecs.open(f_o,"w","utf-8")
    context=fi.readlines()
    for line in context:
        result=line.split()
        line_len=len(result)
        fo.write(line.strip()+" ")
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
                    fo.write(str(i)+" ")
            i=i+1
        fo.write(str(line_len)+"\n")
    fo.close()
    fi.close()

def mode2(f_i):
    fi=codecs.open(f_i,"r","utf-8")
    f_o_prefix=os.path.splitext(f_i)
    f_o=f_o_prefix+r"_wp.txt"
    fo=codecs.open(f_o,"w","utf-8")
    context=fi.readlines()
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
                fo.write(word+" "+pos+"\n")
        fo.write("\n")
    fo.close()
    fi.close()

def mode3(f_i):
    fi=codecs.open(f_i,"r","utf-8")#输入文件是mode1的输出文件
    f_o_prefix=(os.path.splitext(f_i))[0]
    f_o_lb=f_o_prefix+r"_lb.txt"
    f_o_rb=f_o_prefix+r"_rb.txt"
    f_o_context=f_o_prefix+r"_context.txt"
    fo_lb=codecs.open(f_o_lb,"w","utf-8")
    fo_rb=codecs.open(f_o_rb,"w","utf-8")
    fo_context=codecs.open(f_o_context,"w","utf-8")
    context=fi.readlines()
    for line in context:
        result=line.strip().split()
        line_len=int(result[-1])
        begin=0
        end=line_len-1
        #word_field=result[0:line_len]
        loc_field=result[line_len:-1]
        for loc in loc_field:
            left_border=result[max(begin,int(loc)-1)].replace("[","").replace(" ","")
            fo_lb.write(left_border+"\n")
            right_border=result[min(int(loc)+1,end)].replace("[","").replace(" ","")
            fo_rb.write(right_border+"\n")
            ner_context=" ".join(result[max(0,int(loc)-5):min(int(loc)+6,end+1)])
            fo_context.write(ner_context+"\n")
    fo_lb.close()
    fo_rb.close()
    fo_context.close()
    fi.close()

###bash###
#
#   cat [fi] | sort | uniq -c | sort -k1r | grep -v '\]' | grep -v '/[mtxw]' | grep -v ' [[:digit:]] ' | grep -v '/n[stz]' | sed 's/^[ \t]*//g' > [fo]
#   cat [fi] | sed 's/^[ \t]*//g' | cut -d ' ' -f 2 | cut -d / -f 1 > [fo]
#
###bash###

if __name__=='__main__':
    program=os.path.basename(sys.argv[0])
    f_i,parameter,label=sys.argv[1:4]
    if parameter=="1":
        mode1(f_i,label)
    elif parameter=="2":
        mode2(f_i)
    elif parameter=="3":
        mode3(f_i)
    else:
        pass
