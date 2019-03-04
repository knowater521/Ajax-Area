#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# 省市区选择
def index(request):
    return render(request, "areas/index.html", locals())


def pro(request):
    prolist = AreaInfo.objects.filter(parea__isnull=True)
    list = []
    # [[1,'北京']，[2,'天津'],....]  格式自己设计
    for item in prolist:
        list.append([item.id, item.title])
    return JsonResponse({"data":list})   # 构造字典，让JsonResponse序列化返回json
                                         # {"data":[[],[],[],...[]]}


def city(request,id):
    citylist = AreaInfo.objects.filter(parea_id=id)     # parea_id 是字段
    list = []
    # [{id:1,title:北京},{id:2,title:天津},{}...{}]   格式自定义
    for item in citylist:
        list.append({"id":item.id,"title":item.title})
    return JsonResponse({"data":list})      # {"data":[{id:1,title:北京},{id:2,title:天津},{}...{}]}


