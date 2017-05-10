# coding:utf-8 #

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import ns
import ts
import ps

def main(request):
	return render(request,"index/main.html")

def preprocess(request):
    context={}
    request.encoding="utf-8"
    if request.POST:
        label=request.POST['label']
        f_i=request.POST['f_i']
        mode=request.POST['mode']
        if mode=='m1':
            context['preprocess_result']=ps.mode1(f_i,label)
        elif mode=='m2':
            context['preprocess_result']=ps.mode2(f_i)
        else:
            context['preprocess_result']=ps.mode3(f_i)
        context['label']=label
        context['return_f_i']=f_i
    return render(request,"preprocess/preprocess.html",context)

def tokenize(request):
    context={}
    request.encoding="utf-8"
    if request.POST:
        sent=request.POST['sent']
    	context['mm']=ts.mm_tokenize(sent)
    	context['rmm']=ts.rmm_tokenize(sent)
    	context['jieba']=ts.jieba_tokenize(sent)
        context['random']=sent
        context['mecab']=ts.mecab_tokenize(sent)
    else:
        context['random']=ts.random_sent()
    return render(request,"tokenize/tokenize.html",context)

def ner(request):
    context={}
    request.encoding="utf-8"
    if request.POST:
        sent=request.POST['sent']
        context['crf_ner']=ns.naive_crf_ner(sent)
        context['random']=sent
    return render(request,"ner/ner.html",context)

def presentation(request):
    return render(request,"presentation/presentation.html")

def word2vec(request):
    return render(request,"word2vec/word2vec.html")

def semantic(request):
    return render(request,"semantic/semantic.html")

