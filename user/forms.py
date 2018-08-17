from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter user name'}))
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter user email'}))
