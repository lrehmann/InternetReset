import os,re
import urllib
import urllib2
import sys
import time, base64

#This try/except block will first reset the Motorola Modem if the internet works.
#Be sure your modem page can be accessed from http://192.168.100.1 and reset from http://192.168.100.1/reset.htm 
#Only certain modems have this feature, so delete or comment out this block if it doesn't work for your model
try:
	urllib.urlopen("http://74.125.224.72")  #This attempts to access Google by their direct IP address
	print "Fetch Success, Internet Works! :)"
except:
	print "Fetch Error, Internet is currently down :("
	print "\tResetting Modem"
	urllib.urlopen("http://192.168.100.1/reset.htm")
	print "\tModem Reset, waiting 120 seconds to check again..."
	time.sleep(120)

#This block resets OBI Devices. Only uncomment if you are using a OBI VoIP device. Be sure you can access your device at http://192.168.10.1/ (if not, change it to the proper address)
#Enter your correct password in OBIPASSWORD
''' 
OBIPASSWORD="Your password here"
try:
	urllib.urlopen("http://74.125.224.72")
	print "Fetch Success, Internet Works!"
except:
	print "\tInternet Still Down, Resetting OBI"
	handler = urllib2.HTTPDigestAuthHandler()
	handler.add_password("admin@OBi202","http://192.168.10.1/rebootgetconfig.htm","admin", str(OBIPASSWORD))
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	opened=urllib2.urlopen("http://192.168.10.1/rebootgetconfig.htm")
	print "\tOBI Reset, waiting 120 seconds to restart router..."
	time.sleep(60)
'''

#This block resets many Cisco/Linksys routers via the Reboot button on the homepage
#be sure your router can be accessed at http://192.168.1.1 and input your credentials below. 
USERNAME="admin"
PASSWORD="admin" 
try:
	urllib.urlopen("http://74.125.224.72")
	print "Fetch Success, Internet Works!"
except:
	print "\tInternet Still Down, Resetting Router"
	req = urllib2.Request("http://192.168.1.1/apply.cgi")
	base64string = base64.encodestring('%s:%s' % (str(USERNAME), str(PASSWORD)))[:-1]
	authheader =  "Basic %s" % base64string
	req.add_header("Authorization", authheader)
	req.add_data("submit_button=index&change_action=gozila_cgi&submit_type=reboot&timer_interval=30")
	handle = urllib2.urlopen(req)
	print "\tRouter Reset, waiting 120 seconds to update CloudFlare DNS info..."
	time.sleep(60)
	