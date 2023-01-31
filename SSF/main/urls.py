from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('settings/', views.settings),
    path('about/', views.about),
    path('portfolio/<int:id>/', views.portfolio),
    path('portfolio/create/', views.portfolio_create),
    path('collections/', views.collections),
    path('collections/select/<int:id>/<str:name>/<int:b>/<int:mp>/<int:tm>/', views.select_collection),
]
