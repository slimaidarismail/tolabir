from django.contrib.auth import logout
from django.shortcuts import render
from django.views import View


class Home(View):
    template_name = "auth-social-home"

    def get(self, request):
        return render(request, "auth/auth-social.html")

    def post(self, request):
        logout(request)

def privacy(request):
    return render(request, 'privacy.html')

def declaimer(request):
    return render(request, 'declaimer.html')