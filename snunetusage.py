#To login into snulinks internet usage details page and check anyone's internet usages
#Script edited for total usage in one year
import mechanize
import os
import cookielib

auth_user = "YOUR_NETID"
auth_pass = "YOUR_PASSWORD"
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
sign_in = br.open("http://myaccount.snu.edu.in/login.php")
br.select_form(nr = 0)
br["snuNetId"] = auth_user
br["password"] = auth_pass
logged_in = br.submit()
general_page = br.open("http://myaccount.snu.edu.in")
br.select_form(nr = 0)
username = raw_input("Enter the SNU NetID:- ")
br["userNetId"] = username
br["startDate"] = "2015-05-06"
br["endDate"] = "2016-05-05"
re = br.submit()
rs = re.read()
f = open("usage.html",'w')
f.write(rs)
f2 = open("my_usage.html",'a')
f2.write("<p>"+ username + "</p><br><br><br>")
os.system("sed -n '186,202'p usage.html >> my_usage.html")
os.system("rm -r usage.html")
print("Now, you can open the file my_usage.html using a browsing agent(such as Firefox, Chrome, IE8 etc.) from the location where this script exists")
quit()
