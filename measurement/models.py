from __future__ import unicode_literals

import uuid
from django.contrib.postgres.fields import JSONField
from django.db import models
from event.models import Event, Url


class Country(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return u'%s' % self.name

    def __unicode__(self):
        return u'%s' % self.name


class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, related_name='states')

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return u'%s' % self.name

    def __unicode__(self):
        return u'%s' % self.name


class MutedInput(models.Model):

    MED = 'MED'
    DNS = 'DNS'
    TCP = 'TCP'
    HTTP = 'HTTP'

    TYPE_CHOICES = (
        (MED, 'Medicion'),
        (DNS, 'Medicion DNS'),
        (TCP, 'Medicion TCP'),
        (HTTP, 'Medicion HTTP')
    )

    url = models.URLField()
    type_med = models.CharField(verbose_name='Tipo de Medicion',
                                max_length=50,
                                choices=TYPE_CHOICES,
                                default=MED)

    def __unicode__(self):
        return u"%s - %s" % (self.url, self.type_med)


class Plan(models.Model):
    name = models.CharField(max_length=100)
    isp = models.CharField(max_length=100)
    upload = models.CharField(
        verbose_name='Velocidad de Carga publicitado',
        max_length=30)
    download = models.CharField(
        verbose_name='Velocidad de Descarga publicitado',
        max_length=30)
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u"%s" % (self.name)


class Probe(models.Model):

    identification = models.CharField(max_length=50, unique=True)
    region = models.ForeignKey(
        State, related_name='probes', default=3479
    )
    country = models.ForeignKey(
        Country, related_name='probes', default=231
    )
    city = models.CharField(max_length=100)
    isp = models.CharField(max_length=100)
    plan = models.ForeignKey(
        Plan, null=True, blank=True, related_name='probes')

    def __unicode__(self):
        return u"%s - %s" % (self.identification, self.region)


class DNS(models.Model):

    isp = models.CharField(verbose_name='Operadora', max_length=50)
    verbose = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s - %s" % (self.verbose, self.ip)


class Measurement(models.Model):

    _DATABASE = 'titan_db'

    # Test name helper: dns_consistency web_connectivity http_header_field_manipulation http_invalid_request_line
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    input = models.CharField(max_length=50)
    annotations = JSONField()
    report_id = models.CharField(max_length=100)
    report_filename = models.CharField(max_length=150)
    options = models.TextField()
    probe_cc = models.CharField(max_length=50)
    probe_asn = models.CharField(max_length=50)
    probe_ip = models.GenericIPAddressField()
    data_format_version = models.CharField(max_length=10)
    test_name = models.CharField(max_length=25)
    test_start_time = models.DateTimeField()
    measurement_start_time = models.DateTimeField()
    test_runtime = models.FloatField()
    test_helpers = models.TextField()
    test_keys = JSONField()
    software_name = models.CharField(max_length=15)
    software_version = models.CharField(max_length=10)
    test_version = models.CharField(max_length=10)
    bucket_date = models.DateTimeField()

    class Meta:
        db_table = 'metrics'
        managed = False


class Metric(models.Model):

    # Test name helper:
    # dns_consistency
    # web_connectivity
    # http_header_field_manipulation
    # http_invalid_request_line

    measurement = models.CharField(max_length=200)
    input = models.CharField(max_length=50)
    annotations = JSONField()
    report_id = models.CharField(max_length=100)
    report_filename = models.CharField(max_length=150)
    options = models.TextField()
    probe_cc = models.CharField(max_length=50)
    probe_asn = models.CharField(max_length=50)
    probe_ip = models.GenericIPAddressField()
    data_format_version = models.CharField(max_length=10)
    test_name = models.CharField(max_length=25)
    test_start_time = models.DateTimeField()
    measurement_start_time = models.DateTimeField()
    test_runtime = models.FloatField()
    test_helpers = models.TextField()
    test_keys = JSONField()
    software_name = models.CharField(max_length=15)
    software_version = models.CharField(max_length=10)
    test_version = models.CharField(max_length=10)
    bucket_date = models.DateTimeField()
    probe = models.ForeignKey(Probe, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        try:
            probe = self.annotations['probe']
            self.probe = Probe.get(identification=probe)
        except KeyError:
            self.probe = None

        return super(Metric, self).save(force_insert=False, force_update=False, using=None,
                                        update_fields=None)


class Flag(models.Model):

    metric_date = models.DateTimeField()

    # ---------------------------------------------------
    is_flag = models.BooleanField(default=False)
    # True -> hard, False -> soft, None -> muted
    flag = models.NullBooleanField(default=False)
    manual_flag = models.BooleanField(default=False)
    # ---------------------------------------------------

    event = models.ForeignKey(Event, null=True, blank=True,
                              related_name='flags')
    suggested_events = models.ManyToManyField(
        Event, related_name="suggested_events", blank=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.medicion, self.ip, self.type_med)
