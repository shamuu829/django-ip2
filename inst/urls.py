from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # path('', views.login_redirect, name='login_redirect'),
    path('',views.index, name='index'),
    path('',views.profile,name = 'profile'),
    path('',views.timeline,name = 'timeline'),
    path('pic/(\d+)', views.single_pic, name='single_pic'),
    path('comment/(?P<id>\d+)', views.comment, name='comment'),
    # path('user/(\d+)', views.user_details, name='userDetails'),
    path('profile/', views.profile, name='profile'),
    path('single_pic/(\d+)', views.single_pic, name='single_pic'),
    path('send/', views.send, name='send'),
    path('search/', views.search_results, name='search_results'),
    path('upload/profile', views.upload_profile, name='upload_profile'),


]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
