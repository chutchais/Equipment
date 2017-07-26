from django import forms
from .models import Machine
from django.forms.widgets import SelectDateWidget
import datetime

class TicketRequestForm(forms.Form):
    machine = forms.ModelChoiceField(queryset=Machine.objects.all().order_by('name'))
    symptom = forms.CharField(label="Symptom", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'symptom'}))
    details = forms.CharField(label='Details',widget=forms.Textarea,required=False)

    # def __init__(self, *args, **kwargs):
    #     # qs = kwargs.pop('machine')
    #     super(TicketRequestForm, self).__init__(*args, **kwargs)
    #     self.fields['machine'].queryset = qs


class TicketAckForm(forms.Form):
    details = forms.CharField(label='Details',widget=forms.Textarea,required=False)


class TicketStartForm(forms.Form):
    target = forms.DateTimeField(initial=datetime.date.today)
    details = forms.CharField(label='Details',widget=forms.Textarea,required=False)


class TicketFinishForm(forms.Form):
    details = forms.CharField(label='Details',widget=forms.Textarea,required=False)


class TicketCommentForm(forms.Form):
    details = forms.CharField(label='Comment',widget=forms.Textarea,required=False)


    # ,widget=SelectDateWidget(empty_label="Nothing")