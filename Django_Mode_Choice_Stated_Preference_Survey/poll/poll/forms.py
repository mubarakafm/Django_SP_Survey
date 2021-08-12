from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe
#from phonenumber_field.formfields import PhoneNumberField

class homepage_confirmation_form(forms.Form):
    confirmation = forms.BooleanField(label ="")


class mode_choice_form(forms.Form):

    modes = [("Bus","الباص"), ("Car","السيارة")]
    mode_choice = forms.ChoiceField(choices=modes, widget=forms.RadioSelect, label ="الوسيلة المفضلة للرحلة")

class final_page_form(forms.Form):

    email_address = forms.EmailField(label= "الإيميل", required=False)
    twitter_account = forms.CharField(max_length = 30, label ="حساب تويتر", required=False)
