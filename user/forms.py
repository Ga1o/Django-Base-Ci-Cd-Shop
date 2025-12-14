from django import forms


class RegisterForm(forms.Form):
    user_full_name = forms.CharField(max_length=50, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    user_password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Repeat password')
    user_agree = forms.BooleanField(label='Rules agree', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class LoginForm(forms.Form):
    user_email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')


class CheckSecretCodeForm(forms.Form):
    secret_code = forms.CharField(label='Code', widget=forms.TextInput(attrs={'class': 'form-control'}))


class ForgotPasswordForm(forms.Form):
    user_email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))


class NewPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='New password')
    new_password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Repeat new password')
