from django import forms
from manager.models import BookTable

class BookTable(forms.ModelForm):

    class Meta:
        model = BookTable
        fields = ('name', 'email', 'phone', 'date', 'time', 'people_numb', 'message')
