from django import forms
from manager.models import BookTable
from user_message.models import UserMessage

class BookTableForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100, 
        min_length=2,
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "name",
            "class": "form-control",
            "id": "name",
            "placeholder": "Your Name",
            "data-rule": "minlen:4",
            "data-msg": "Please enter at least 4 chars"
        }))
    
    email = forms.EmailField(
        max_length=100, 
        min_length=10,
        widget=forms.EmailInput(attrs={
            "type": "email",
            "class": "form-control",
            "name": "email",
            "id": "email",
            "placeholder":"Your Email",
            "data-rule": "email",
            "data-msg": "Please enter a valid email"
        }))
    
    phone = forms.CharField(
        max_length = 20,
        min_length=10,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "name": "phone",
            "id": "phone",
            "placeholder": "Your Phone: XXX-XXX-XXXX",
            "data-rule": "minlen:4",
            "data-msg": "Please enter at least 4 chars"
        }))
    
    people_numb = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            "type": "number",
            "class": "form-control",
            "name": "people",
            "id": "people",
            "placeholder": "# of people",
            "data-rule": "minlen:1",
            "data-msg": "Please enter at least 1 chars"
        }))

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "text",
            "name": "date",
            "class": "form-control",
            "id": "date",
            "placeholder": "Date: dd/mm/yy",
            "data-rule": "minlen:4",
            "data-msg": "Please enter at least 4 chars"
         }))
    
    time = forms.TimeField(
        required = False,
        widget=forms.TimeInput(attrs={
            "type": "text",
            "class": "form-control",
            "name": "time",
            "id": "time",
            "placeholder": "Time: hh:mm",
            "data-rule": "minlen:4",
            "data-msg": "Please enter at least 4 chars"
        }))

    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "name": "message",
            "rows": "5",
            "placeholder": "Message"
        }))
    

    class Meta:
        model = BookTable
        fields = ('name', 'email', 'phone', 'date', 'time', 'people_numb', 'message')


class UserMessageForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100,
        min_length=2,
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "name",
            "class": "form-control",
            "id": "name",
            "placeholder": "Your Name"
        }))

    email = forms.EmailField(
        max_length=100, 
        min_length=10,
        widget=forms.EmailInput(attrs={
            "type": "email",
            "class": "form-control",
            "name": "email",
            "id": "email",
            "placeholder": "Your Email"
        }))

    subject = forms.CharField(
        max_length=100,
        min_length=2,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "name": "subject",
            "id": "subject",
            "placeholder": "Subject"
        }))

    message = forms.CharField(
        max_length=300,
        min_length=2,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "name": "message",
            "rows": "5",
            "placeholder": "Message"
        }))

    class Meta:
        model = UserMessage
        fields = ('name', 'email', 'subject', 'message')



