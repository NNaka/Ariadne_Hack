import re, time, datetime, csv, base64
from pylab import savefig
from django.utils import timezone
from django.http import HttpResponse
from betterbirth.models import Mother
from betterbirth.models import Baby
from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
import os, sys

key_exp = '''([A-Z]+)'''
value_exp = ''':[\s]*(\S[\S\s]*)'''
first_name_exp = '''([A-Z,a-z]+)\s[A-Z, a-z]+'''
last_name_exp = '''[A-Z,a-z]+\s([A-Z, a-z]+)'''

mother1 = Mother(phone_num=1123456789, mother_condition='Cramps', age=29, postal_code='07016', first_name='Jane',last_name='Smith', give_aid=True, receive_aid=True, home_city='New York');
mother1.save();
baby1 = Baby(mother=mother1, baby_gender='Male', conception_datetime=datetime.datetime.now(), birth_of_baby=False)
baby1.save();
mother2 = Mother(phone_num=19745325461, mother_condition='Stomach Ache', age=18, postal_code='07016', first_name='Emily',last_name='Jones', give_aid=True, receive_aid=True, home_city='New York');
mother2.save();
baby2 = Baby(mother=mother2, baby_gender='Male', conception_datetime=datetime.datetime.now(), birth_of_baby=False)
baby2.save();
mother3 = Mother(phone_num=12435564534, mother_condition='Healthy', age=32, postal_code='12345', first_name='Robin',last_name='Brown', give_aid=True, receive_aid=True, home_city='New York');
mother3.save();
baby3 = Baby(mother=mother3, baby_gender='Male', conception_datetime=datetime.datetime.now(), birth_of_baby=False)
baby3.save();
mother4 = Mother(phone_num=19562451654, mother_condition='Healthy', age=30, postal_code='84653', first_name='Karen',last_name='Cummings', give_aid=True, receive_aid=True, home_city='New York');
mother4.save();
baby4 = Baby(mother=mother4, baby_gender='Male', conception_datetime=datetime.datetime.now(), birth_of_baby=False)
baby4.save();
mother5 = Mother(phone_num=12645765487, mother_condition='Healthy', age=25, postal_code='07016', first_name='Emily',last_name='Goldstein', give_aid=True, receive_aid=True, home_city='New York');
mother5.save();
baby5 = Baby(mother=mother5, baby_gender='Male', conception_datetime=datetime.datetime.now(), birth_of_baby=False)
baby5.save();
mother6 = Mother(phone_num=1563456765, mother_condition='Numb Toes', age=25, postal_code='07016', first_name='Hannah',last_name='Chang', give_aid=True, receive_aid=True, home_city='New York');
mother6.save();
baby6 = Baby(mother=mother6, baby_gender='Male', conception_datetime=datetime.datetime.now(), birth_of_baby=False)
baby6.save();

def makecsv(request):
	plt.clf()
	os.remove('/home/alex/Desktop/AriadneHack/Uttar/betterbirth/piechart.png')
	babies = Baby.objects.all()
	now = time.time()
	first = 5
	second = 5
	third = 5
	for item in babies:
		conception = int(item.conception_datetime.strftime("%s"))		
		diff = now - conception
		if (diff < 3000):
			first+=1
		elif (diff < 5000):
			second +=1
		else:
			third += 1

	trimester_list = '"1","' + str(first) + '"\n"2","' + str(second) + '"\n"3","' + str(third) + '"\n'
	f = open('/home/alex/Desktop/AriadneHack/Uttar/betterbirth/data.csv', 'w')
	f.write(trimester_list);
	f.close()

	f = open('/home/alex/Desktop/AriadneHack/Uttar/betterbirth/data.csv')
	reader = csv.reader(f)
	rows = [];
	for line in reader:
		rows.append(line[1])
# Casting string list to double list
	rows = map(float, rows)
	total = sum(rows)
		
	labels = 'Third Trimester', 'Second Trimester', 'First Trimester'
	sizes = [rows[2]/total*100, rows[1]/total*100, rows[0]/total*100]
	colors = ['darkblue', 'blue', 'lightskyblue']
	#explode = (0, 0.1, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

	plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
	# Set aspect ratio to be equal so that pie is drawn as a circle.
	plt.axis('equal')

	savefig('/home/alex/Desktop/AriadneHack/Uttar/betterbirth/piechart.png', )
	with open("betterbirth/piechart.png", "rb") as image:
		encoded_string = base64.b64encode(image.read())
	f.close();
	title = '''<div><h1 align=center>Pregnancy and Birth Visualization in India</h1></div>'''
	title_1 = '''<div><h2 align=center>Pregnancy Distribution Based on Time Pregnant</h2></div>'''
	image = '''<div><a><img src="data:image/png;base64,'''+encoded_string+'''" alt="Distribution"/></a></div>'''
	title_2 = '''<div><h2 align=center>Birth Rate based on Population and Mortality Rate</h2></div>'''
	plot = '''<div><div>
    <a href="https://plot.ly/~hcohen21/75/" target="_blank" title="" style="display: block; text-align: center;"><img src="https://plot.ly/~hcohen21/75.png" alt="" style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="hcohen21:75" src="https://plot.ly/embed.js" async></script>
</div>
</div>'''
	return HttpResponse(title + title_1 + image + title_2 + plot)


@twilio_view
def sms(request):
	message_body = request.GET.get('Body', '')
	from_number = request.GET.get('From', '')
	from_zip = request.GET.get('FromZip', '')
	from_city = request.GET.get('FromCity', '')
	mothers = Mother.objects.all()
	found = False
	for item in mothers:
		if (int(item.phone_num) == int(from_number[1:])):
			mother = item
			found=True
			break
	if not found:
		mother = Mother(phone_num = from_number, postal_code = from_zip, home_city = from_city)
		mother.save()
		baby = Baby(mother = mother, conception_datetime = time.time())
		baby.save()
	babies = Baby.objects.all()
	found = False
	for item in babies:
		if (int(item.mother.phone_num) == int(from_number[1:])):
			baby = item
			found=True
			break
	if not found:
		baby = Baby(mother = mother, conception_datetime = time.time())
	key = re.findall(key_exp, message_body, re.I|re.DOTALL)

	if (key):
		key = key[0]	
	value = re.findall(value_exp, message_body, re.I|re.DOTALL)
	if (value):
		value = value[0]	

	r = Response()

	if (key == "NAME"):
		first_name = re.findall(first_name_exp, value, re.I|re.DOTALL)[0]
		last_name = re.findall(last_name_exp, value, re.I|re.DOTALL)[0]
		mother.first_name = first_name
		mother.last_name = last_name
		mother.save()		
		r.message(first_name + " " + last_name + "  recorded!")
		return r
	if (key == "AGE"):
		mother.age = value
		mother.save()
		r.message(value + "  recorded!")
		return r
        
	if (key == "GIVEAID"):
		mother.give_aid=value
		mother.save()
		r.message(value + "  recorded!")
		return r
                
	if (key == "RECEIVEAID"):
		mother.receive_aid=value
		mother.save()
		r.message(value + "  recorded!")
		return r
        
	if (key == "MOTHERCONDITION"):
		mother.mother_condition=value
		mother.save()
		r.message(value + "  recorded!")
		return r

	if (key == "GENDER"):
		baby.baby_gender=value
		print ("HERE")
		baby.save()
		r.message(value + "  recorded!")
		return r

	if (key == "BIRTH"):
		baby.birth_of_baby=value
		baby.birth_datetime=timezone.now()
		baby.save()
		r.message("Congratulations!")
		return r

	if (key == "HEIGHT"):
		baby.baby_height=value
		baby.save()
		r.message(value + "  recorded!")
		return r

	if (key == "WEIGHT"):
		baby.baby_weight=value
		baby.save()
		r.message(value + "  recorded!")
		return r

	if (key == "BABYCONDITION"):
		baby.baby_health=value
		baby.save()
		r.message(value + "  recorded!")
		return r

	if (key == "MOTHERSTATUS"):
		mother2 = Mother.objects.all().filter(phone_num=from_number)[0]
		fields = mother2._meta.get_all_field_names()
		msg = ''
		for field in fields:
			if (field != 'baby'):
				msg += field + ': ' + str(getattr(mother2,field)) + "\n"
		r.message(msg)
		return r
	if (key == "BABYSTATUS"):
		baby = Baby.objects.all().filter(mother = mother)

		if (baby):
			baby = baby[0]
			fields = baby._meta.get_all_field_names()
			msg = ''
			for field in fields:
				msg += field + ': ' + str(getattr(baby,field)) + "\n"
			r.message(msg)
			return r
		else:
			r.message("You have no baby")
			return r

	if (key == "NEEDHELP"):
		r = Response()
		now = time.time()
		conception = int(item.conception_datetime.strftime("%s"))		
		diff = now - conception
		if (diff < 1000):
			msg = "First Trimester Information:\n"
			msg += "Some symptoms you might be feeling include:\n"
			msg += "Extreme tiredness; tender, swollen breasts; upset stomach; cravings or distate for certain foods; mood swings; constipation; need to pass urine more often; headache; heartburn; weight gain or loss\n"
			msg += "For more information, visit: http://www.mayoclinic.org/healthy-living/pregnancy-week-by-week/in-depth/pregnancy/art-20047208"
			r.message(msg)
		elif (diff < 4000):
			msg = "Second Trimester Information:\n"
			msg += "Some symptoms you might be feeling include:\n"
			msg += "Body aches, such as back, abdomen, breasts, thighs, or buttocks; Stretch marks; Darkening of hte skin around your nipples; A line on the skin running from belly button to pubic hairline; numb or tingling hands, caleed carpal tunnel syndrome\n"
			msg += "For more information, visit: http://www.mayoclinic.org/healthy-living/pregnancy-week-by-week/in-depth/fetal-development/art-20046151"
			r.message(msg)
		elif (diff < 8000):
			msg = "Third Trimester Information:\n"
			msg += "Some symptoms you might be feeling include:\n"
			msg += "Shortness of breath, heartburn; swelling of the ankles, fingers, and face; hemorrhoids; your belly button may stick out; trouble sleeping; contractions, which can be a sign of real or false labor\n"
			msg += "For more information, visit: http://www.mayoclinic.org/healthy-living/pregnancy-week-by-week/in-depth/fetal-development/art-20045997"
			r.message(msg)
		else:
			msg = "Next Steps Information:\n"
			msg += "Congratulations!  You had a baby!  Here are some suggestions:\n"
			msg += "Make sure to wash your hands to prevent infections; it's important to carefully support your baby's head and neck; it has been proven that women who seek help have higher success rate, so don't be afraid to reach out!\n"
			msg += "For more information, visit: http://www.mayoclinic.org/healthy-living/pregnancy-week-by-week/in-depth/fetal-development/art-20045997"
			r.message(msg)
		return r

	if (key == "EMERGENCY"):
		r = Response()
		r.message("Go to the hospital!")		
		return r

	if (key == "FINDFRIEND"):
		me = Mother.objects.all().filter(phone_num=from_number)[0]
		if not me.receive_aid:
			r = Response()
			r.message('Your preferences state you do not want help. Consider texting RECEIVEAID:True to this number')
			return r
		friends = []
		r = Response()
		mothers = Mother.objects.all().filter(give_aid=True);
		found = False
		for item in mothers:
			if (int(item.postal_code) == int(from_zip)):
				friends.append(item)
				found=True

		if not found:
			r.message("Unfortunately nobody is available") 
			return r
		message = "Here are some people you can contact:\n"
		for friend in friends:
			if (int(friend.phone_num) != int(from_number[1:])):
				message += friend.first_name + "'s phone number is " + str(friend.phone_num) + '\n'			
		r.message(message)
		return r

	if (key == "OPTIONS"):
		r = Response()
		msg = "Message Format - 'KEYWORD:value'\n"
		msg += "Keyword List\n"
		msg += "NAME - Enter your first and last name separated by a whitespace\n"
		msg += "AGE - Enter your numeric age\n"
		msg += "GIVEAID - Enter 'True' if you wish to help other mothers near you. Defaults to 'False'\n"
		msg += "RECEIVEAID - Enter 'True' if you wish to be helped by other mothers. Defaults to 'True'\n"
		msg += "MOTHERCONDITION - Enter how you feel\n"
		msg += "GENDER - Enter the gender of your child\n"
		msg += "BIRTH - Simply send this keyword when your child is born\n"
		msg += "HEIGHT - Enter the height of your child in centimeters\n"
		msg += "WEIGHT - Enter the weight of your child in grams\n"
		msg += "BABYCONDITION - Enter how your baby feels\n"
		msg += "MOTHERSTATUS - See what your profile looks like\n"
		msg += "BABYSTATUS - See what your child's profile looks like\n"
		msg += "NEEDHELP - Receive helpful tips based on how far along you are\n"
		msg += "EMERGENCY - Go to the hospital!\n"
		msg += "FINDFRIEND - Find mothers nearby willing to lend a hand\n"
		r.message(msg)
		return r	
