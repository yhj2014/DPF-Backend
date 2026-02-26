from django import forms
from django.utils.translation import gettext_lazy as _

class SignUp(forms.Form):
    username = forms.CharField(label=_('用户名'), max_length=20, min_length=2)
    mail = forms.EmailField(label=_('邮箱'), max_length=64)
    password = forms.CharField(label=_('密码'), max_length=30)