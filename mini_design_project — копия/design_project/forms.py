from django import forms


class Contact(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Name*'}))
    phone = forms.IntegerField(required=True,
                               widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}))
    mail = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'mail'}))
    text = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'message-box'}))
