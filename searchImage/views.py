import os
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from django import forms
import numpy as np
import caffehelper
import bkmeanshelper
from django.core.files.storage import default_storage
import sesdemo.settings


center_only = False
tmp_dir = "tmp/"
predict_dir = os.path.join(sesdemo.settings.BASE_DIR,tmp_dir)

predict_fname = ""


def upload(request):
    #print request.GET['fileName']
    if(request.method == 'POST'):
        fname = request.FILES.get('input_1234[]', "xxxx")
        print fname
        predict_fname = fname.name
        #image_data=[]
        #for fdata in fname:
        #    image_data = image_data + fdata
        ret = "success"
        with default_storage.open(tmp_dir + fname.name, 'wb+') as destination:
            for chunk in fname.chunks():
                destination.write(chunk)

        inputs = caffehelper.load_image(predict_dir+ predict_fname)
        result = caffehelper.classifier.predict(inputs, not center_only)
        print result
        binary_code = caffehelper.to_binary_int64s(result[0])
        bkmeanshelper.findKNN(binary_code)

        return JsonResponse(ret, safe=False)
    else:
        return render_to_response('base.html')

