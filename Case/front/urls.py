from django.conf.urls import url
import views


urlpatterns = [
    url(
        r'^create/$',
        views.CreateCase.as_view(),
        name='create-case'
    ),
    url(
        r'^$',
        views.ListCase.as_view(),
        name='list-case'
    ),
    url(
        r'^(?P<pk>[0-9]+)/detail/$',
        views.DetailCase.as_view(),
        name='detail-case'
    ),
    url(
        r'^(?P<pk>[0-9]+)/change-status/$',
        views.ChangeCaseStatus.as_view(),
        name='change-case-status'
    ),
    url(
        r'^(?P<pk>[0-9]+)/change-status-detail/$',
        views.ChangeCaseStatusDetail.as_view(),
        name='change-case-status-detail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/delete/$',
        views.DeleteCase.as_view(),
        name='delete-case'
    ),
]
