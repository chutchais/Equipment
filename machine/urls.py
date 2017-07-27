from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^request/$', views.create, name='create'),
    url(r'^pending/machine/(?P<machine>[-\w|\W\ ]+)$', views.pending_repair_by_machine, name='pending_repair_by_machine'),
    url(r'^pending/(?P<machine_type>[-\w|\W\ ]+)$', views.pending_repair, name='pending_type'),
    url(r'^pending/$', views.pending_repair, name='pending_all'),
    url(r'^repair/$', views.pending_repair, name='pending_repair'),
    url(r'^repair/(?P<id>[-\w|\W\ ]+)/ack$', views.acknowledge, name='acknowledge'),
    url(r'^repair/(?P<id>[-\w|\W\ ]+)/comment$', views.commentRepair, name='comment_repair'),
    url(r'^repair/(?P<id>[-\w|\W\ ]+)/finish$', views.finishRepair, name='finish_repair'),
    url(r'^repair/(?P<id>[-\w|\W\ ]+)$', views.startRepair, name='start_repair'),
    url(r'^details/(?P<machine>[-\w|\W\ ]+)/(?P<id>[-\w|\W\ ]+)$', views.machineDetails, name='machine_details_id'),
    url(r'^details/(?P<machine>[-\w|\W\ ]+)$', views.machineDetails2, name='machine_details'),
    url(r'^status/(?P<machine_type>[-\w|\W\ ]+)$', views.machineStatus, name='machine_Status'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm} , name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/machine'},name='logout'),
    ]


