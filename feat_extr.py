# coding:utf-8 #

import codecs
import re

def feat_extr(file_in,file_out,*feat):
    fin=codecs.open(file_in,"r","utf-8")
    fout=codecs.open(file_out,"w","utf-8")
    context=fin.readlines()
    for line in context:
        insert=[]
        result=line.split()
        i=0
        for token in result:
            pattern=re.match("(.*?)\[.*",token)
            if i==0:
                insert.append(token)
            elif token=="__BOS__" or token=="__EOS__":
                insert.append(token)
            elif pattern:
                if pattern.group(1) in feat:
                    insert.append(token)
            else:
                pass
            i=1
        fout.write("\t".join(insert)+"\n")
    fout.close()
    fin.close()
