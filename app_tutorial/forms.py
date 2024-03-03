
from django.forms import ModelForm
from .models import Subjects,Topics,Entries
from django.core.exceptions import ValidationError

class SubjectsForm(ModelForm):
    class Meta:
        model = Subjects
        fields = ['subject']

class TopicsForm(ModelForm):
    class Meta:
        model = Topics
        fields = ['subject', 'section',]

class EntriesForm(ModelForm):
    class Meta:
        model = Entries
        fields = ['subject', 'section',  'info', 'code', 'links']    



#form content verification
