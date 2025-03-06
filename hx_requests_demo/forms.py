from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    @property
    def helper(self):

        helper = FormHelper()
        helper.form_tag = False
        return helper
