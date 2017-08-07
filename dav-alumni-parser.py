import requests
import sys
from time import time
from termcolor import colored
from bs4 import BeautifulSoup
import pymysql
import warnings
#warnings.filterwarnings("ignore")
aid=0
count=0
ids=0
max_records=200

t_global = time()
print "Establishing a secured connection to the server"
t0 = time()
db = pymysql.connect(host='localhost',user='root',passwd='')
cursor = db.cursor()
print colored("CONNECTION TO server ESTABLISHED","green")
print "Checking if the database 'davnerul' exists"
query = ("CREATE DATABASE IF NOT EXISTS davnerul")
cursor.execute(query)
query = ("USE davnerul")
cursor.execute(query)
print colored("Database validation successful","green")
print "Checking for table 'details' in the current database"
query = ("CREATE TABLE IF NOT EXISTS details (ID varchar(5) not null primary key, Name varchar(200) not null, Institution varchar(500), Occupation varchar(1000), LastAttendedYear varchar(20), LastAttendedClass varchar(30), Gender enum('Male','Female'), MaritalStatus varchar(30), Email varchar(500), DOB varchar(20), Phone varchar(15), Mobile varchar(15), Address varchar(1000), About varchar(1000))")
cursor.execute(query)
print colored("The table 'details' is successfully configured and ready for writing","green")
print "Preprocessing completed in ", round(time()-t0, 3), " seconds"

fields=['Name','Institution','Occupation','LastAttendedYear','LastAttendedClass','Gender','MaritalStatus','Email','DOB','Phone','Mobile','Address','About']

print colored("Populating the database","white")
for aid in range(1,max_records+1):
	db = pymysql.connect(host='localhost',user='root',passwd='')
	cursor = db.cursor()
	query = ("USE davnerul")
	cursor.execute(query)
	query = "select * from details where ID='"+str(ids+1)+"'"
	records = cursor.execute(query)
	if records > 0:
		ids+=1
		continue
	count=0
	tmpdict = {'Name':'', 'Institution':'', 'Occupation':'', 'LastAttendedYear':'', 'LastAttendedClass':'', 'Gender':'', 'MaritalStatus':'', 'Email':'', 'DOB':'', 'Phone':'', 'Mobile':'', 'Address':'', 'About':''}
	
	url_to_scrape = 'http://davnerul.com/Alumni-User-Detail.aspx?aid='+str(aid)
	r = requests.get(url_to_scrape)
	soup = BeautifulSoup(r.text,"lxml")
	table_main = soup.find("table")
	for td in soup.find_all("span"):
		tmpdict[fields[count]] = "".join(td.strings)
		if(tmpdict['Name']==''):
			print colored("Database cloning completed in "+str(round(time()-t_global, 3))+" seconds","green")
			exit(0)
		count+=1
	query = "INSERT INTO details values('"+str(ids+1)+"','"+tmpdict['Name']+"','"+tmpdict['Institution']+"','"+tmpdict['Occupation']+"','"+tmpdict['LastAttendedYear']+"','"+tmpdict['LastAttendedClass']+"','"+tmpdict['Gender']+"','"+tmpdict['MaritalStatus']+"','"+tmpdict['Email']+"','"+tmpdict['DOB']+"','"+tmpdict['Phone']+"','"+tmpdict['Mobile']+"','"+tmpdict['Address']+"',\""+tmpdict['About']+"\")"
	print colored(str(ids+1)+". Inserting "+tmpdict['Name']+"'s records to the database","yellow")
	print query+"\n"
	cursor.execute(query)
	db.commit()
	ids+=1
print colored("Database cloning completed in "+str(round(time()-t_global, 3))+" seconds","green")
