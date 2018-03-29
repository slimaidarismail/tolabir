from django.contrib.auth import logout
from django.shortcuts import render
from .models import Test, Answer
from random import randint
import time
from .models import UserProfile
import os
import urllib
from PIL import Image
import requests

# Create your views here.
from django.views import View


class Home(View):
    template_name = 'home_page'

    def get(self, request):
        tests = Test.objects.order_by('id')
        return render(request, 'tafaha/home.html',{'tests':tests})

class SingleTest(View):
    template_name = "single-test"

    def get(self, request, id):
        try:
            test = Test.objects.get(id=id)
        except Test.DoesNotExist:
            return render(request, 'tafaha/single-test.html')
        else:
            return render(request, 'tafaha/single-test.html', {'test': test})

class Loading(View):
    template_name = "loading"

    def post(self, request, id):
        return render(request, 'tafaha/loading.html', {'id': id})

class Result(View):
    template_name = "result"

    def post(self, request , id):

        test = Test.objects.get(id=id)
        #get user picture
        f = open("img/profile/"+request.user.id+'profile.jpg', 'wb')  # create file locally
        img_url = 'http://graph.facebook.com/'+request.user.UID+'/picture?type=large&width=400'
        f.write(requests.get(img_url).content)  # write image content to this file
        f.close()

        #get random choice
        choice = Answer.objects.filter(test=test).order_by('?').first()

        #save the resault
        files = [
            choice.picture,
            "img/profile/"+request.user.id+'profile.jpg',
        ]
        result = Image.new("RGB", (800, 420))
        i = True

        for index, file in enumerate(files):
            path = os.path.expanduser(file)
            img = Image.open(path)
            if i:
                img.thumbnail((800, 420), Image.ANTIALIAS)
                i = False
            else:
                img.thumbnail((290, 270), Image.ANTIALIAS)
            x = index % 2 * 518
            y = index * 40
            w, h = img.size
            result.paste(img, (x, y, x + w, y + h))

        result.save(os.path.expanduser('img/resaults/'+request.user.UID+id+'.jpg'))



        return render(request, 'tafaha/result.html')

