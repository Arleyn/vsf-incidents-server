from django import forms
from event.models import Event, Site
from measurement.models import Flag


class EventForm(forms.ModelForm):
    """EventForm: ModelForm of Event model"""

    open_ended = forms.BooleanField(widget=forms.CheckboxInput(),
                                    required=False)
    flags = forms.CharField(widget=forms.TextInput(attrs={'class': 'hidden'}),
                            required=True, label="")

    class Meta:
        model = Event
        fields = ['open_ended', 'identification', 'flags', 'type']

    def clean(self):
        '''Data from EventForm'''

        form_data = self.cleaned_data

        # If form is valid then check if flags are the same
        # target, isp and type. Otherwise, show a not valid
        # form error.

        if self.is_valid():

            # Format flags from the form.

            flags = form_data['flags'].split(' ')

            bd_flags = []

            # Get flags from database with same target, isp
            # and type

            for f in filter(None, flags):
                split = f.split('&')
                bd_flags += Flag.objects.filter(medicion=split[0],
                                                target__url=split[1],
                                                isp=split[2],
                                                ip=split[3],
                                                type_med=split[4])

            if bd_flags:

                # If not all flags are the same target, isp and type then
                # show an error.

                if not all(map(lambda f: f.target == bd_flags[0].target and f.isp == bd_flags[0].isp
                               and f.type_med == bd_flags[0].type_med, bd_flags[1:])):
                    self.add_error(None,
                                   'Selected measurements must have the same targets, types and ISP')

        else:
            self.add_error(None,
                       'The Event must have measurements and identification asociated')


class EventExtendForm(forms.ModelForm):
    TYPE_CHOICES = (
        ('MED', 'MED'),
        ('DNS', 'DNS'),
        ('TCP', 'TCP'),
        ('HTTP', 'HTTP')
    )
    open_ended = forms.BooleanField(widget=forms.CheckboxInput(),
                                    required=False)
    flags_type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        required=False,
        label='Chance all Measurements type to:')

    class Meta():
        model = Event
        fields = ['open_ended', 'identification', 'isp', 'type']


class EventEvidenceForm(forms.ModelForm):
    """
    EventEvidenceForm: ModelForm of Event model adding url model attributes
    to create event target.
    This is used to create/update an event with external evidence
    """
    open_ended = forms.BooleanField(widget=forms.CheckboxInput(),
                                    required=False)

    target_url = forms.URLField(
        label="Target URL",
        required=False)
    target_ip = forms.GenericIPAddressField(
        label="Target IP",
        required=False)
    target_site = forms.ModelChoiceField(
        queryset=Site.objects.all(),
        empty_label="(Nothing)",
        label="Target Site",
        required=False)

    class Meta():
        model = Event
        exclude = [
            'draft',
            'target'
        ]

