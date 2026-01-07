from django import forms
from .models import Users

# ---------------- Sign Up ----------------
class SignUpForm(forms.ModelForm):
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
    )

    class Meta:
        model = Users
        fields = ['Name', 'Email', 'Phone', 'Password']
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'Email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'Phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['Password'])  # hashed password
        if commit:
            user.save()
        return user

# ---------------- Login ----------------
class LoginForm(forms.Form):
    Email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
    )
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
    )