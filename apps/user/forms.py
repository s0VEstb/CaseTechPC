from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.user.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm # Импортируем стандартную форму входа

class RegisterForm(UserCreationForm):

    avatar = forms.ImageField(label='Аватар', required=False)
    username = forms.CharField(label='Имя пользователя', max_length=150, required=True)
    email = forms.EmailField(label='Email адрес', required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'avatar']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    def save(self, commit=True):
        # This method is crucial. UserCreationForm.save() handles creating the user
        # and hashing passwords. We need to handle the 'avatar' separately
        # because UserCreationForm doesn't know about it.

        # First, save the user without the avatar (as avatar is not in UserCreationForm's default fields)
        user = super().save(commit=False) # commit=False so we can modify the user object

        # Now, handle the avatar. If avatar data exists in the form's cleaned_data,
        # assign it to the user instance.
        if 'avatar' in self.cleaned_data and self.cleaned_data['avatar']:
            user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save() # Save the user with the avatar
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

