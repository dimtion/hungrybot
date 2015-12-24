from django.contrib import admin
from django import forms
from django.db import models
from django.forms import TextInput, Textarea

from .models import *

# We design admin model for each model

class choice_str_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(choice_str_form, self).__init__(*args, **kwargs)
        self.fields['text'].widget = admin.widgets.AdminTextareaWidget()
    # class Meta:
    #     model = choice_str
    #     widget = {
    #         'text': Textarea(attrs={'cols': 100, 'rows': 3}),
    #     }
    #     fields = ['text', 'nb_choice']

class choice_str_admin(admin.ModelAdmin):
    form = choice_str_form

    
class sentence_only_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(sentence_only_form, self).__init__(*args, **kwargs)
        self.fields['text'].widget = admin.widgets.AdminTextareaWidget()

        
class sentence_only_admin(admin.ModelAdmin):
    form = sentence_only_form
        
        
# Then we register
admin.site.register(choice_str, choice_str_admin)
admin.site.register(hello_morning, sentence_only_admin)
admin.site.register(what_morning, sentence_only_admin)
admin.site.register(what_dejeuner, sentence_only_admin)
admin.site.register(entree_str, sentence_only_admin)
admin.site.register(plat_str, sentence_only_admin)
admin.site.register(dessert_str, sentence_only_admin)
admin.site.register(hello_dinner, sentence_only_admin)
admin.site.register(what_dinner, sentence_only_admin)


