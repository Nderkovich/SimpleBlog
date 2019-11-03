from django.urls import path
from mylogin import views


app_name='mylogin'


urlpatterns=[
    path('login/',views.login_view, name='login' ),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]