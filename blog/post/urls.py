from django.urls import path
from post import views

app_name = 'post'


urlpatterns = [
    path('post/<int:post_id>' , views.post_detail,name='post_detail'),
    path('add_post/', views.add_post, name="add_post"),
    path('my_posts/', views.post_view, name='my_posts'),
    path('user_posts/<int:user_id>',views.user_posts, name='user_posts'),
    path('', views.all_posts, name="all_posts"),
]