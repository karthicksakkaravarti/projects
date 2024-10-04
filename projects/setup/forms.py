from django import forms

from django import forms

class SetupForm(forms.Form):
    app_name = forms.CharField(label='App Name', max_length=100, required=True)
    is_setup_complete = forms.BooleanField(label='Is Setup Complete', required=False)
    app_logo = forms.ImageField(label='App Logo', required=False)
    app_favicon = forms.ImageField(label='App Favicon', required=False)

    admin_email = forms.EmailField(max_length=254, required=True, label='Admin Email')
    admin_password = forms.CharField(widget=forms.PasswordInput, required=True, label='Admin Password')

