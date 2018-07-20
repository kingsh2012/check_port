import json
from django.shortcuts import render

# Create your views here.
# <view logic> return HttpResponse('result')

from django.http import HttpResponse
from django.views.generic import View
from readnginx.tasks import read_nginx, git_pull_config
from pubstatus.tasks import get_status
from django.views.decorators.csrf import csrf_exempt



class data_update(View):
    def get(self, request):
        return render(request, template_name='readnginx/data_update.html')
    def post(self, request):
        try:
            data = json.loads(request.body)
            method = data["method"]
            if method=="git_pull":
                git_pull_config.delay()
            elif method=="read_nginx":
                read_nginx.delay()
            elif method=="check_port":
                get_status.delay()
            return HttpResponse(status=200)
        except Exception as e:
            return str(e)
