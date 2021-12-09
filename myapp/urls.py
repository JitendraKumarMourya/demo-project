from . import views
from django.urls import path
urlpatterns = [
    path('hello',views.TextFun,name='hello my page'),
    path('index',views.IndexFun,name='index'),
    path('login',views.LoginFun,name='login'),
    path('demoimage',views.DemoimageFun,name="demoimage"),
    path('project_demo',views.ProjectFun,name="project_demo"),

    path('demo/',views.demofn,name="demo"),
]