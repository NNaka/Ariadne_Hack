# -*- coding: utf-8 -*-
import re, time
from betterbirth.models import Mother
from betterbirth.models import Baby
from django.shortcuts import render

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

key_exp = '''([\S]+):'''
value_exp = ''':[\s]*(\S[\S\s]*)'''
first_name_exp = '''(\S)+\s'''
last_name_exp = '''\s(\S)+'''

@twilio_view
def sms(request):
	message_body = request.GET.get('Body', '')
	from_number = request.GET.get('From', '')
	from_zip = request.GET.get('FromZip', '')


	key = re.findall(key_exp, message_body, re.I|re.DOTALL)[0]
	value = re.findall(value_exp, message_body, re.I|re.DOTALL)[0]
	

	r = Response()
	print(from_zip)
	r.message(from_number + " " + from_zip + " " + key + " " + value)

	if (key == "NAME"):
		mother = Mother(phone_num=from_number, first_name=value)	
		mother.save()		

        if (key == "AGE"):
                mother = Mother(phone_num=from_number, age=value)
                mother.save()
        
        if (key == "POSTALCODE"):
                mother = Mother(phone_num=from_number, postal_code=value)
                mother.save()
        
        if (key == "GIVEAID"):
                mother = Mother(phone_num=from_number, give_aid=value)
                mother.save()
                
        if (key == "RECEIVEAID"):
                mother = Mother(phone_num=from_number, receive_aid=value)
                mother.save()
        
        if (key == "MOTHERCONDITION"):
                mother = Mother(phone_num=from_number, mother_condition=value)
                mother.save()
        
	return r
