from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from mod_auth import views
from pubstatus import views
from readnginx import views as readnginx_views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^data_update$', readnginx_views.data_update.as_view(), name='data_update'),
]

urlpatterns += staticfiles_urlpatterns()
