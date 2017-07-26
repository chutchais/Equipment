from django.conf.urls import url
from django.contrib import admin

from familys.api.views import (
	FamilyListAPIView,
	)

urlpatterns = [
	url(r'^$', FamilyListAPIView.as_view(), name='list'),
]