from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_evento, name='addEvento'),
    url(r'^edit/(?P<pk>\d+)$', views.evento_update, name='edit_evento'),
    url(r'^delete/(?P<pk>\d+)$', views.evento_delete, name='delete_evento'),
]