from django.urls import path
from . import views
urlpatterns = [
    # path('', views.account),
    path('signup/', views.SignUpView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.logout),
]
