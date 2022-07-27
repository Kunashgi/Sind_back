from django.urls import re_path as url
from Data import views
from django.conf.urls.static import static

urlpatterns = [
  url(r'^mesa1$', views.mesa1Api),
  url(r'^mesa1/([0-9]+)$', views.mesa1Api),
]