from django.urls import path, re_path
from . import views

app_name = 'api'

urlpatterns = [
    path('test', views.test_add),
    re_path(r'^news/?(?P<news_id>[1-9][0-9]*)?/?$', views.NewsApiView.as_view(), name='news_api')
]
