from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.image_detail,name='detail'),
    url(r'^create/$',views.image_create,name='create'),
    


]