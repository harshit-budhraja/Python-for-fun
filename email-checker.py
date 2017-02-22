#To connect to https://email-checker.net page and check if the entered email is VALID or not
import mechanize
import os
import cookielib

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
sign_in = br.open("http://email-checker.net/")
br.select_form(nr = 0)
email = raw_input("Enter an email id:- ")
br["email"] = email
validate_email = br.submit()
result = validate_email.read()
f = open("usage.html",'w')
f.write(result)
f2 = open("my_usage.html",'a')
os.system("sed -n '84'p usage.html >> my_usage.html")
os.system("rm -r usage.html")
os.system("cat my_usage.html | cut -c 33-46")
os.system("rm -r my_usage.html")
#os.system("cat my_usage.html | cut -c 47-95")
#print("Now, you can open the file my_usage.html using a browsing agent(such as Firefox, Chrome, IE8 etc.) from the location where this script exists")
quit()
