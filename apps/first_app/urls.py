
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.display),
    url(r'^courses$', views.submit),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^bye$', views.delete),
    url(r'^comments$', views.comments),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^process2/(?P<id>\d+)$', views.process2),

]
