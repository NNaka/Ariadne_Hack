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






