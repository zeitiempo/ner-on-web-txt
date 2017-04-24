# coding:utf-8 #

import re
import codecs
import sys

def nertag_gen_c5(pos):
    if pos.startswith("nr"):
        return "PER","n"
    elif pos.startswith("ns"):
        return "LOC","n"
    elif pos.startswith("nt"):
        return "ORG","n"
    elif pos.startswith("nz"):
        return "ONE","n"
    else:
        return "OOO",pos

def nertag_gen_c2(pos): # remove ONE from NER
    if pos.startswith("nr") or pos.startswith("nr") or pos.startswith("nt"):
        return "NER","n"
    else:
        return "ONE","n"

#def nertag_gen_fine_grained(pos):

def fourtag_gen(word_len,index):
    if word_len==1:
        return "S"
    elif index==0:
        return "B"
    elif index==word_len-1:
        return "E"
    else:
        return "M"

def tag_gen(in_name,out_name,nertag_gen):
    fin=codecs.open(in_name,"r","utf-8")
    fout=codecs.open(out_name,"w","utf-8")
    context=fin.readlines()
    for line in context:
        result=line.split()
        for token in result:
            pair=re.match("(.*?)/(.*)",token)
            if pair:
                word=pair.group(1).replace("[","").replace(" ","")
                word_len=len(word)
                pos=pair.group(2)
                pos_modify=re.match("(.*)\].*",pos)
                if pos_modify:
                    pos=pos_modify.group(1)
                nertag,pos=nertag_gen(pos)
                index=0
                for char in word:
                    fourtag=fourtag_gen(word_len,index)
                    fout.write(char+" "+fourtag+" "+pos+" "+fourtag+"-"+nertag+"\n")
                    index=index+1
        fout.write("\n")
    fout.close()
    fin.close()

if __name__=='__main__':
    program=os.path.basename(sys.argv[0])
    in_f,out_f=sys.argv[1:3]
    tag_gen(in_f,out_f,nertag_gen_c2)
