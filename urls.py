from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/increase_like/(?P<pk>\d+)/$', views.increase_like, name='increase_like'),#like 
     url(r'^post/increase_dislike/(?P<pk>\d+)/$', views.increase_dislike, name='increase_dislike'),#dislike 
    url(r'^post/new/$', views.post_new, name='post_new'),#forms
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),#post_edit template
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),#comment
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),#comment approve
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),#comment remove
]