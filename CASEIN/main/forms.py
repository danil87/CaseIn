from .models import Members
from django.forms import TextInput, ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms



class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-mail', 'autocomplete': "off"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-mail', 'autocomplete': "off"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))
    name = forms.CharField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'Имя'}))
    surname = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    dolznost = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Должность'}))
    class Meta:
        model = Members
        fields = ['username', 'password1', 'password2', 'name', 'surname', 'dolznost', 'Zadanie1', 'Zadanie2', 'Zadanie3', 'Zadanie4']

class MembersForm(ModelForm):
    class Meta:
        model = Members
        fields = ['email', 'name', 'surname', 'dolznost', 'Zadanie1', 'Zadanie2', 'Zadanie3', 'Zadanie4']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "dolznost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "Zadanie1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задание 1(+/-)'
            }),
            "Zadanie2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задание 2(+/-)'
            }),
            "Zadanie3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задание 3(+/-)'
            }),
            "Zadanie4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задание 4(+/-)'
            })
        }
