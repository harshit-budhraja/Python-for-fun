#To login into snulinks internet usage details page and check anyone's internet usages
import mechanize
import os
import cookielib
import commands

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
#Authentication details
br["snuNetId"] = "YOUR_NETID"
br["password"] = "YOUR PASSWORD"
logged_in = br.submit()
general_page = br.open("http://myaccount.snu.edu.in")
username = raw_input()
br.select_form(nr = 0)
br["userNetId"] = username 
br["startDate"] = "2015-07-07"
br["endDate"] = "2016-07-06"
re = br.submit()
rs = re.read()
f = open("usage.html",'w')
f.write(rs)
f.close()
usage = commands.getoutput("sed -n '198'p usage.html | awk '{print $6}' | cut -c 5-10")
try:
	use = float(usage)
except(ValueError, TypeError):
	usage = commands.getoutput("sed -n '198'p usage.html | awk '{print $6}' | cut -c 5-9")
os.system("rm -r usage.html")
print("The total usage of the provided student is: %s GB" % usage)
quit()
