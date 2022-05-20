from django.urls import URLPattern, path,include
from .views import *
from django.contrib import admin

app_name='product'
urlpatterns=[
    path("hello/",ProductListAPI.as_view()),
    path("test/",upload_file),
    path("project/<email>/",test,name='home'),
    path("project/<email>/pic/",test2),
    path("project/<email>/take/",test3),

]
