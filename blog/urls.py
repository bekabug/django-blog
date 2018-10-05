from django.urls import path

from . import views
urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('',  views.style_guide, name="style_guide"),
]