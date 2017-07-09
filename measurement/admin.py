from django.contrib import admin
from models import (
    DNS, Flag, Probe, State, Country, Plan, ISP, Metric,
)


class MetricAdmin(admin.ModelAdmin):
    list_filter = ('test_name', 'probe__identification')
    search_fields = ('measurement', 'input')


class FlagAdmin(admin.ModelAdmin):
    list_filter = ('flag', 'manual_flag')
    search_fields = ('metric__measurement', 'metric__input')


admin.site.register(DNS)
admin.site.register(Flag, FlagAdmin)
admin.site.register(Probe)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Plan)
admin.site.register(ISP)
admin.site.register(Metric, MetricAdmin)
