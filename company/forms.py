from django import forms

class TestForm(forms.Form):
    name = forms.CharField(label="姓名")
    email = forms.EmailField(label="邮箱")