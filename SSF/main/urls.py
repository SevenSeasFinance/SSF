from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('settings/', views.settings),
    path('about/', views.about),
    path('portfolio/create/', views.portfolio_create),
    path('collections/', views.collections),
    path('collections/select/<int:id>/<str:name>/<int:b>/<int:mp>/<int:tm>/', views.select_collection),
         # /collections/select/1/Thamer/1/1/1/
    # path("profiles/create/", views.profile),
    # path("profiles/<int:landmark_id>/", views.landmark),
    # path("about/", views.about),
    # path("settings/", views.settings),
]
