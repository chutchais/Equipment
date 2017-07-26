from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^request/$', views.create, name='create'),
    url(r'^pending/$', views.pending, name='pending'),
    url(r'^pending/(?P<id>[-\w|\W\ ]+)$', views.acknowledge, name='acknowledge'),
    url(r'^repair/$', views.pending_repair, name='pending_repair'),
    url(r'^repair/(?P<id>[-\w|\W\ ]+)/comment$', views.commentRepair, name='comment_repair'),
    url(r'^repair/(?P<id>[-\w|\W\ ]+)/finish$', views.finishRepair, name='finish_repair'),
    url(r'^repair/(?P<id>[-\w|\W\ ]+)$', views.startRepair, name='start_repair'),
    url(r'^details/(?P<machine>[-\w|\W\ ]+)/(?P<id>[-\w|\W\ ]+)$', views.machineDetails, name='machine_details_id'),
    url(r'^details/(?P<machine>[-\w|\W\ ]+)$', views.machineDetails, name='machine_details'),

    ]


