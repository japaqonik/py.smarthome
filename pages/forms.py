from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                 'placeholder':'Password'}))


class LightSwitching(forms.Form):
    bedroom = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();',
                                                                   'class':'custom-control-input',
                                                                   'id':'customSwitch2'}))
