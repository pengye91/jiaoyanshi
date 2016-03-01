from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^posts/', views.posts),
    url(r'^$', views.index),
    url()
]
