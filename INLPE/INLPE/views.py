# coding:utf-8 #

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import ns
import ts

def main(request):
	return render(request,"index/main.html")

def preprocess(request):
	return render(request,"preprocess/preprocess.html")

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
        context['crf_ner']=ns.crf_ner(sent)
        context['random']=sent
    return render(request,"ner/ner.html",context)

def presentation(request):
	return render(request,"presentation/presentation.html")

