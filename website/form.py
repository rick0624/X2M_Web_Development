from dataclasses import field
from django import forms
from .models import New
from django.forms import ModelForm
from .models import New,Contact
from .models import *

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title', 'keyword', 'content', )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'message', )
    
    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(ContactForm, self).clean()

        # extract the username and text field from the data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        message = self.cleaned_data.get('message')
 
        # conditions to be met for the username length
        '''if len(first_name) < 2:
            self._errors['first_name'] = self.error_class([
                '請填寫姓名'])
        if len(last_name) < 2:
            self._errors['last_name'] = self.error_class([
                '請填寫名字'])
        if len(phone) < 5 :
            self._errors['phone'] = self.error_class([
                '請填寫電話'])
        if len(message) < 5 :
            self._errors['message'] = self.error_class([
                '請填寫訊息'])'''
        #return self.cleaned_data