#from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response


#from django.forms import *
from dojango.forms import *


class SIPAddForm(Form):
    extension = IntegerField(
        required=True, 
        help_text="Enter extension number")
    secret = IntegerField(
        required=True, 
        help_text="Enter password for extension",
        widget = PasswordInput(
            attrs={
                'invalidMessage' : 'Password should be a number',
                'class': 'customClass'
                }) 
        )

    my_field = DateField(
        required=True, 
        help_text="Enter a valid date!", 
        widget=DateInput(
            attrs={
                'invalidMessage': 'The date is invalid!', 
                'class': 'customClass'
            }
        ))
        

def add(req, **kw):
    f =  SIPAddForm()
    return render_to_response('sip/add.html', {'form': f } )
