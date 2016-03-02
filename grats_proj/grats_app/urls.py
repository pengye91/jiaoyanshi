from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^posts/', views.posts, name='all_posts'),
    url(r'^$', views.index, name='app_index'),
    url(r'^detail/', views.link_detail, name='details')
]
