# -*- coding: utf-8 -*-
# RafKac
# wprost z dokumentacji Django
# https://docs.djangoproject.com/pl/3.2/topics/class-based-views/generic-editing/


from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
