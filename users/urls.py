# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^change/(?P<username>[\w.@+-]+)/$',
        view=views.UserChangeView.as_view(),
        name='change'
    ),

    # URL pattern for the UserDeleteView
    url(
        regex=r'^delete/(?P<username>[\w.@+-]+)/$',
        view=views.UserDeleteView.as_view(),
        name='delete'
    ),

    # URL pattern for the UserCreateView
    url(
        regex=r'^~create/$',
        view=views.UserCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the CreateReportView
    url(
        regex=r'^~create_report/$',
        view=views.CreateReportView.as_view(),
        name='report'
    ),
]