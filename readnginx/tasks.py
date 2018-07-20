#-*-coding:utf-8-*-

from checkport.celery import app
from readnginx.handle import main_pipeline, git_pull
from readnginx.test_handle import main_pipeline_test, git_pull_test

@app.task()
def read_nginx():
    return (main_pipeline() and main_pipeline_test())

@app.task()
def git_pull_config():
    return (git_pull() and git_pull_test())
