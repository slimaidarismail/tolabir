from django.contrib.auth import logout
from django.shortcuts import render
from .models import Test, Answer
from random import randint
from PIL import Image, ImageFont
from PIL import ImageDraw
import time
from .models import UserProfile

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

    def post(self, request, response , id):
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])

        return render(request, 'tafaha/result.html', {'user': url})

