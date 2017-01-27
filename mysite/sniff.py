#!/usr/bin/env python
#coding=utf-8
import pcap
import dpkt
import os
import re
import requests
import sqlite3
import datetime
import thread
from time import *
#define variable
TCP_HTTP_PORT = 80
GLB_victims_num = 0
GLB_victims_mac = []
Flag = 1
#add new victim's mac to dic
def add_mac(mac):
	if mac in GLB_victims_mac:
		return 0
	else:
		GLB_victims_mac.append(mac)
		return 1
def judge_url(url):
	if '.gif' in url or '.js' in url or '.css' in url or '.jpg' in url or '.png' in url or '.swf' in url or len(url) > 100 or '.aspx' in url:
		return 0
	else:
		return 1 
def set_flag(threadName,):
	
	global Flag
	sleep(0.02)
	Flag = 0
	sleep(0.5)
	Flag = 1
	print "********************************************************************"

'''
def dowloadPic(imageUrl,filePath):
    r = requests.get(imageUrl) or die("error")
    with open(filePath, "wb") as code:
        code.write(r.content)
'''

#link to database
conn = sqlite3.connect("db.sqlite3") 

#listen to sniff packet
pc = pcap.pcap()
b = 'tcp port 80'
pc.setfilter(b)
#victim number
num = 0
icmp6 = dpkt.icmp6.ICMP6()
icmp = dpkt.icmp.ICMP()
#loop to analyse packet
for ts,buf in pc:
	eth = dpkt.ethernet.Ethernet(buf)
	ip = eth.data
	tcp = ip.data
	#judge the packet whether is tcp link
	if len(tcp) > 0 and type(tcp) != type(icmp) and type(tcp)!=type(icmp6) and tcp.dport == TCP_HTTP_PORT:
		if(len(tcp.data)>0):
			num += 1
			ip_add = '%d.%d.%d.%d'%(ord(ip.src[0]),ord(ip.src[1]),ord(ip.src[2]),ord(ip.src[3]))
			mac = '%x:%x:%x:%x:%x:%x'%(ord(eth.src[0]),ord(eth.src[1]),ord(eth.src[2]),ord(eth.src[3]) , ord(eth.src[4]),ord(eth.src[5]) )
			print ip_add
			print num
			print mac
			print ts
			try:
				http = dpkt.http.Request(tcp.data) or die("cant extract")
				if  len(http.headers)>0 and 'user-agent'  in http.headers and 'host' in http.headers:
					useragent = re.findall('\(([^&]{1,})\)',http.headers['user-agent']) 
					time = datetime.datetime.now()
					url = http.headers['host']+http.uri
					add_mac(mac)

					if mac in GLB_victims_mac and judge_url(url):
						sql1 = "insert into Record_urls(id,url,time)values("+str(GLB_victims_mac.index(mac)+1)+",'"+url+"','"+str(time)+"')"
						thread.start_new_thread(set_flag,("jugde",))
						conn.execute(sql1)
						conn.commit()


					if len(useragent) > 0:
						
						print useragent[0]
						print url
						cur = conn.cursor() 
						test = "select * from victim where mac ='"+mac+"'"
						cur.execute(test)
						result = cur.fetchone()
						if not result:
							global GLB_victims_num
							GLB_victims_num += 1
							sql = "insert into victim(id,useragent,mac,time,ip)values('"+str(GLB_victims_num)+"','"+useragent[0]+"','"+mac+"','"+str(time)+"','"+str(ip_add)+"')"  
							
							
							conn.execute(sql)
							conn.commit()

					'''	
					if 'jpg' in http.uri.lower():
						dowloadPic('http:/'+http.uri,str(i)+'.jpg')
						print "****************************************************"
					if 'png' in http.uri.lower():
						dowloadPic('http:/'+http.uri,str(i)+'.png')'''

			except dpkt.dpkt.UnpackError:
				continue

'''			
for ts,pkt in pc:
#    print `dpkt.ethernet.Ethernet(pkt)`
    Eth = dpkt.ethernet.Ethernet(pkt)
    length = Eth.data.len
    tcp = Eth.data.data
#    print type(length)
    if length > 48 and tcp.data:
    	
        content = str(tcp.data)
        #http = dpkt.http.Request(tcp.data)
        #print http.uri
        if 'GET' in content:
            url = content.split()[1]
            print url
            fp.write(url+'\r\n')
            fp.flush()
#        print '--------------------------------------------------'
#        print str(`Eth.data.data.data`)
#        print str(`Eth.data.data.data`).split()[1]
#        print '--------------------------------------------------'
fp.close()
'''