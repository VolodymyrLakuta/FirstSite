from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username'].strip()
        password = self.cleaned_data['password'].strip()

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                return forms.ValidationError('Username or password is wrong')
        return super().clean()


class UserRegistrationForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_rep = forms.CharField(widget=forms.PasswordInput())


    def clean_password_rep(self):
        data = self.cleaned_data
        if data['password'] == data['password_rep']:
            return data['password_rep']

        return forms.ValidationError('Passwords must be equals')

    class Meta:
        model = User
        fields = ('username', )
