from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class SignupForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(SignupForm, self).clean(*args, **kwargs)