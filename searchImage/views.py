from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from django import forms

def upload(request):
    #print request.GET['fileName']
    if(request.method == 'POST'):
        fname = request.FILES.get('input_1234[]', "xxxx")
        print fname
        image_data=[]
        for fdata in fname:
            image_data.append(fdata)
        ret = "success"
        return JsonResponse(ret, safe=False)
    else:
        return render_to_response('base.html')

