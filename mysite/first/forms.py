from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Threads
        fields = ['thread_name', 'm_max']


class AddThreadForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [ 'user_id','message', 'syga']
        #widgets = {'user_id': forms.HiddenInput() } #скрытие форм


"""
class AddPostForm(forms.Form):
    thread_name = forms.CharField()
    m_max = forms.IntegerField()


class AddThreadForm(forms.Form):
    parent = forms.ModelChoiceField(queryset=Threads.objects.all())
    message = forms.CharField()
    syga = forms.BooleanField(required=False)

"""
