from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.logins,name='login'),
    path('signup/',views.signup,name='signup'),
    path('feedback/',views.feedback,name='feedback'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)