from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('User.html', views.User,name='User'),
    path('quiz.html',views.Quiz,name='Quiz'),
    path('result.html',views.result,name='result')
]
