from django import forms

#your code goes here
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'placeholder':'username', 'class':'form-field'}), label='')

    password = forms.CharField(max_length = 50, widget = forms.PasswordInput(attrs={'placeholder':'password', 'class':'form-field'}), label='')
