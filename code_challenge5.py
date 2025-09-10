print("Welcome to manga reader!")
genre = input("What genre do you want?(Action/Sci-fi/Romcom): ").lower()
#action
if genre == "action":
	length = input("How long?(Short/Medium/Long): ").lower()
	if length == 'short':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend 666 Satan (O-Parts Hunter, 76 ch, 2001–2007)")
		if year == 2010:
			print("I recommend Attack on Titan: Before the Fall (17 vols, 2013–2019)")
	if length == 'medium':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend Tenjou Tenge (136 ch, 1997–2010)")
		if year == 2010:
			print("I recommend Seraph of the End (120+ ch, 2012–ongoing)")
	if length == 'long':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend One Piece (1997–ongoing, 1000+ ch)")
		if year == 2010:
			print("I recommend Black Clover (350+ ch, 2015–ongoing)")
#Sci-fi
elif genre == "sci-fi":
	length = input("How long?(Short/Medium/Long): ").lower()
	if length == 'short':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend Blame! (66 ch, 1997–2003)")
		if year == 2010:
			print("I recommend Ultraman (short arcs, 2011–ongoing)")
	if length == 'medium':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend Eden: It’s an Endless World! (127 ch, 1998–2008)")
		if year == 2010:
			print("I recommend DARWIN’S GAME (100+ ch, 2012–ongoing)")
	if length == 'long':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend Fullmetal Alchemist (116 ch, 2001–2010 — technically medium but iconic long-read)")
		if year == 2010:
			print("I recommend Dr. Stone (232 ch, 2017–2022)")
#romcom
elif genre == "romcom":
	length = input("How long?(Short/Medium/Long): ").lower()
	if length == 'short':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend Midori Days (85 ch, 2002–2004)")
		if year == 2010:
			print("I recommend Horimiya (122 ch, 2011–2021)")
	if length == 'medium':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend Love Hina (118 ch, 1998–2001)")
		if year == 2010:
			print("I recommend Kaguya-sama: Love is War (281 ch, 2015–2022)")
	if length == 'long':
		year = eval(input("Which decade?(2000/2010): "))
		if year == 2000:
			print("I recommend Haruhi Suzumiya manga (2004–2013, many vols, romcom + supernatural)")
		if year == 2010:
			print("I recommend Domestic Girlfriend (276 ch, 2014–2020, dramatic romcom)")
else:
	print("Sorry, I can't find what you're looking for.")






