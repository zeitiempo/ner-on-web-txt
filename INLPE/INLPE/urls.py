"""INLPE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import views
import settings 

urlpatterns = [
    url(r'^main/',views.main),
    url(r'^preprocess/',views.preprocess),
    url(r'^tokenize/',views.tokenize),
    url(r'^ner/',views.ner),
    url(r'^presentation/',views.presentation),
    url(r'^word2vec/',views.word2vec),
    url(r'^semantic/',views.semantic),
]
