from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Evidence, Battle


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['title', 'description', 'category', 'icon']
        exclude = ['legalUser']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['year', 'verdict']
        exclude = ['legalUser']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']