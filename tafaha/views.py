from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render

from spam.settings import BASE_DIR
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

class Logout(View):
    template_name = 'logout'

    def post(self, request):
        logout(request)
        return render(request, 'tafaha/home.html')


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
        user = request.user

        #get user picture
        social = user.social_auth.get(provider='facebook')
        userid = social.uid

        # create file locally
        f = open(os.path.join(BASE_DIR, "assets/img/profile/")+str(userid)+'profile.jpg', 'wb')
        img_url = 'http://graph.facebook.com/'+str(userid)+'/picture?type=large&width=400'
        f.write(requests.get(img_url).content)  # write image content to this file
        f.close()

        #get random choice
        choice = Answer.objects.filter(test=test).order_by('?').first()

        #save the resault
        img_name = str(choice.picture.url).split('/')[4]
        files = [
            os.path.join(BASE_DIR, "assets/img/tafaha/") + str(img_name),
            os.path.join(BASE_DIR, "assets/img/profile/")+str(userid)+'profile.jpg',
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

        result.save(os.path.join(BASE_DIR, "assets/img/results/")+str(userid)+str(test.id)+'.jpg')
        result_image_url = "img/results/"+str(userid)+str(test.id)+'.jpg'

        return render(request, 'tafaha/result.html', {'result': result_image_url})

