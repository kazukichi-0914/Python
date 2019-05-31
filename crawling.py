
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
	
import urllib2
import socket
import time
import sys, traceback
import sqlite3
import subprocess
import socket
 
URL1 = "http://sudeni.todai.in/ranklink.cgi?id=kazu914"
 
URL2 =  "http://ameblo.jp/akimotoo0726"
 
URL3 = "http://ameblo.jp/massuuu-yuttan"
 
URL4 = "http://ameblo.jp/miyazawafamily"
 
URL5 = "http://ameblo.jp/dance-ayapon"
 
URL6 = "https://www.google.co.jp/search?q=%E3%81%8B%E3%81%9A%E3%81%8D%E3%81%A1%E3%80%82%E3%81%AE%E6%97%A5%E8%A8%98&oq=%E3%81%8B%E3%81%9A%E3%81%8D%E3%81%A1%E3%80%82%E3%81%AE%E6%97%A5%E8%A8%98&aqs=chrome..69i57j69i65.5120j0j3&sourceid=chrome&es_sm=91&ie=UTF-8"
 
URL7= "http://ameblo.jp/rematador"
 
response1 = urllib2.urlopen(URL1)
print " check"
time.sleep(10)
 
response2 = urllib2.urlopen(URL2)
print " check"
time.sleep(10)
 
response3 = urllib2.urlopen(URL3)
print " check"
time.sleep(10)
 
response4 = urllib2.urlopen(URL4)
print " check"
time.sleep(10)
 
response5 = urllib2.urlopen(URL5)
print " check"
time.sleep(10)
 
response6 = urllib2.urlopen(URL6)
print " check"
time.sleep(10)
 
response7 = urllib2.urlopen(URL7)
print " check"
time.sleep(10)
