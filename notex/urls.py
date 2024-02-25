from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('sign/',views.sign,name='sign'),
    path('logined',views.userlogin,name='success'),
]


