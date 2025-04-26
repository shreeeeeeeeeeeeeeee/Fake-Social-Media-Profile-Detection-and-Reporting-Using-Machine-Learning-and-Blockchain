from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # Registration page as homepage
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('form/', views.input_form, name='form'),
    path('chat/', views.chat_view, name='chat'),
    path('report/', views.report_fake_profile, name='report'),
]
