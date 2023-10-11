from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('register',views.register,name='register'),
    path('login',views.loginView,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.logoutView,name='logout'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

