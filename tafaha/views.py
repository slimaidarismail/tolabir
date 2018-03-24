from django.contrib.auth import logout
from django.shortcuts import render
from .models import Test, Answer
from random import randint
from PIL import Image, ImageFont
from PIL import ImageDraw
import time

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
            return render(request, 'tafaha/single-test.html', { 'test' : test})

class Loading(View):
    template_name = "loading"

    def post(self, request, id):
        return render(request, 'tafaha/loading.html', {'id': id})

class Result(View):
    template_name = "result"
    
    def post(self, request, id):
        answers = Answer.objects.filter(test=id) #number of answers of this test
        rand = randint(0, answers.count()-1)
        selected_answer = answers[rand]
        # draw on the image
        image_name = str(request.user.id).strip()+str(time.time()*1000)[:-5]
        img = Image.open(selected_answer.picture)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("assets/fonts/Cairo-Black.ttf", 40)
        string = " سيمتلك هذه السيارة "
        draw.text((50, 310), str(string), (252, 97, 0), font=font)
        img.save('assets/img/tafaha/'+image_name.strip()+'.jpg')

        return render(request, 'tafaha/result.html', {'answer': selected_answer, 'img': image_name})