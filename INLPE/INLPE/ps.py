# coding:utf-8 #

import re

def mode1(f_i,label):
    context=f_i.split("\n")
    hidden=[]
    for line in context:
        hidden_line=''
        result=line.split()
        line_len=len(result)
        hidden_line=hidden_line+line.strip()+" "
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
                    hidden_line=hidden_line+str(i)+" "
            i=i+1
        hidden_line=hidden_line+str(line_len)
    hidden.append(hidden_line)
    output=''
    for new_line in hidden:
        hidden_result=new_line.strip().split()
        hidden_line_len=int(hidden_result[-1])
        begin=0
        end=hidden_line_len-1
        loc_field=hidden_result[hidden_line_len:-1]
        for loc in loc_field:
            left_border=hidden_result[max(begin,int(loc)-1)].replace("[","").replace(" ","")
            output=output+left_border+"\n"
            right_border=hidden_result[min(int(loc)+1,end)].replace("[","").replace(" ","")
            output=output+right_border+"\n"
    return output

def mode2(f_i):
    output=''
    context=f_i.split("\n")
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
                output=output+word+" "+pos+"\n"
        output=output+"\n"
    return output

def mode3(f_i):
    output=''
    context=f_i.split()
    for line in context:
        end=len(line.strip())-1
        i=0
        for char in line.strip():
            if end==0:
                output=output+char+" S\n"
            elif i==0:
                output=output+char+" B\n"
            elif i==end:
                output=output+char+" E\n"
            else:
                output=output+char+" M\n"
            i=i+1
    return output
