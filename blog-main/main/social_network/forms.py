from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from social_network.models import Message


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image']

    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Ваша почта')
    password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())
    image = forms.ImageField(label='Аватарка')


class CommentsForm(forms.ModelForm):
    text = forms.CharField(label='Оставить сообщение', widget=forms.Textarea(attrs={'cols': 100, 'rows': 5, 'placeholder': 'Сообщение'}))

    class Meta:
        model = Message
        fields = ['text', 'image']
        labels = {
            'image': 'Изображение',
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError('Комментарий не должен быть пустым.')
        return text


class UpdateForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    date_birth = forms.DateField(label='Дата вашего рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    status = forms.CharField(label='Статус')
    about = forms.CharField(label='О себе', widget=forms.Textarea(attrs={'cols': 65, 'rows': 10, 'placeholder': 'Введите текст'}))
    image = forms.ImageField(label='Аватарка', required=False)



