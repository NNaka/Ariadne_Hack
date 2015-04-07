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

	if (key == "GENDER"):
		baby = Baby(baby_gender=value)
		baby.save()

	if (key == "BIRTH");
		baby = Baby(birth_of_baby=value)
		baby.save()

	if (key == "HEIGHT");
		baby = Baby(baby_height_cm=value)
		baby.save()

	if (key == "HEALTH");
		baby = Baby(baby_health=value)
		baby.save()

	if (key == "BIRTHDATE");
		baby = Baby(birth_datetime=value)
		baby.save()

	#need conditionals for conception and assinging mother				

				

	return r
