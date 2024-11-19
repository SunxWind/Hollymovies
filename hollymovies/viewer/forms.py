import re

from django.core.exceptions import ValidationError
from django.forms import (
  CharField, DateField, Form, ModelForm, IntegerField, ModelChoiceField, Textarea, TextInput, EmailInput, PasswordInput, ModelForm, DateInput
)

from viewer.models import Genre, Movie, Actor
from django.contrib.auth.forms import UserCreationForm

class MovieModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
    # title = CharField(max_length=128)
    # genre = ModelChoiceField(queryset=Genre.objects)
    # rating = IntegerField(min_value=1, max_value=10)
    # released = DateField()
    # description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        # Každá věta bude začínat velkým písmenem
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'commedy' and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError(
                "Commedies aren't so good to be rated over 5."
            )
        return result


class MovieForm(MovieModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ActorModelForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }


class ActorForm(ActorModelForm):

    # class Meta:
    #     model = Actor
    #     fields = '__all__'
    #     widgets = {
    #         'birth_date': DateInput(attrs={'type': 'date'})
    #     }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class GenreModelForm(Form):
    name = CharField(max_length=128)


class GenreForm(GenreModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']
        """
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'first_name', 'email', 'last_name', 'password1', 'password2']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

