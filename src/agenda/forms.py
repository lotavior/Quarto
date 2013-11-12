'''
Created on 12/11/2013

@author: otavio.ferreira
'''
from django import forms
from django.contrib.auth.models import User
from agenda.models import ItemAgenda

class ModelMultipleUserField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, user):
        return "%s (%s)" % (user.get_full_name(), user)

class FormItemAgenda(forms.ModelForm):
    data = forms.DateField(
                           widget=forms.DateInput(format='%d/%m/%Y'),
                           input_formats=['%d/%m/%Y', '%d/%m/%y'])
    
    participantes = ModelMultipleUserField(queryset=User.objects.all())
    
    class Meta:
        model = ItemAgenda
        fields = ('titulo', 'data', 'hora', 'descricao', 'participantes')