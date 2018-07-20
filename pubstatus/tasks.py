#-*-*-coding:utf-8-*-*-
from checkport.celery import app
from pubstatus.handle import checkport
from pubstatus.models import instance
from readnginx.handle import main_pipeline

@app.task()
def get_status():
    instances = instance.objects.all()
    for i in instances:
        status = checkport(i.host,i.port)
        if status == True and i.status != 2:
            i.status=2
            i.save()
        elif status == False and i.status != 3:
            i.status=3
            i.save()
    return True


