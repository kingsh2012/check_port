from django.shortcuts import render

# Create your views here.
# <view logic> return HttpResponse('result')

from django.http import HttpResponse
from django.views.generic import View
from pubstatus.models import *

class index(View): 
    def get(self, request):
        env = request.GET.get("env", 'online')
        instances = instance.objects.filter(env_flag=env)
        return render(request, 'pubstatus/index.html', {"instances":instances, "env":env})
