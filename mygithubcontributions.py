import mechanize
import os
import commands

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Chrome/6.0.472.63")]
general_page = br.open("http://github.com/harshitbudhraja/")
rs = general_page.read()
f = open("usage.html",'w')
f.write(rs)
f.close()
contri = commands.getoutput("sed -n '333'p usage.html | awk '{print $1}'")
try:
	use = int(contri)
except(ValueError, TypeError):
	quit()
os.system("rm -r usage.html")
print("The total contributions is :- %d" % use)
quit()
