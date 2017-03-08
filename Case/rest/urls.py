from django.conf.urls import url
from Case.rest import views

urlpatterns = [
    url(
        r'^list/$',
        views.ListCaseView.as_view(),
        name='list-case-rest'
    ),
    url(
        r'^detail/(?P<case_id>[0-9]+)/$',
        views.DetailCaseRestView.as_view(),
        name='detail-case-rest'
    ),
    url(
        r'^detail_event/(?P<case_id>[0-9]+)/$',
        views.DetailEventCaseRestView.as_view(),
        name='detail-event-case-rest'
    ),
    url(
        r'^detail_update/(?P<case_id>[0-9]+)/$',
        views.DetailUpdateCaseRestView.as_view(),
        name='detail-update-case-rest'
    ),
    url(
        r'^region/$',
        views.ListRegionView.as_view(),
        name='region-rest'
    ),
    # url(
    #     r'^list/region/$',
    #     views.ListRegionCaseView.as_view(),
    #     name='list-region-case-rest'
    # ),
    url(
        r'^events/region/(?P<case_id>[0-9]+)/$',
        views.ListCountEventsByRegionByCase.as_view(),
        name='events-regions'
    ),
    url(
        r'^category/$',
        views.ListCategoryView.as_view(),
        name='category-rest'
    ),
    url(
        r'^list/category/$',
        views.ListCategoryCaseView.as_view(),
        name='list-category-case-rest'
    ),
    url(
        r'^isp/$',
        views.ListISPView.as_view(),
        name='isp-rest'
    ),
    url(
        r'^list/isp/$',
        views.ListISPCaseView.as_view(),
        name='list-isp-case-rest'
    ),
    url(
        r'^list-case-filter/$',
        views.ListCaseFilterView.as_view(),
        name='list-case-filter-rest'
    ),
    url(
        r'^gantt/(?P<case_id>[0-9]+)/$',
        views.GanttChart.as_view(),
        name='gantt'
    ),
    url(
        r'^events-month/(?P<case_id>[0-9]+)/$',
        views.EventsByMonth.as_view(),
        name='events-month'
    ),
]
