#!/usr/bin/python

import telnetlib
import re
#import sys

#attenPort = int(sys.argv[1])
#value = int(sys.argv[2])

#from __main__ import *

def writeAtten(a,b):

    attenPort = a
    value = b

    #print 'This: %s %s' % (attenPort, value)

    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('SAR%s %s\n' % (attenPort, value))
    telnet.write('DIS\n')
    txt = telnet.read_all()

    telnet.close()

    # URL that generated this code:
    # http://txt2re.com/index-python.php3?s=Escape%20character%20is%20%27^]%27.%2050PA-684%20Connection%20Open%20Atten%231%20=%20127%20dB&13


    re1='.*?'   # Non-greedy match on filler
    re2='\\d+'  # Uninteresting: int
    re3='.*?'   # Non-greedy match on filler
    re4='\\d+'  # Uninteresting: int
    re5='.*?'   # Non-greedy match on filler
    re6='\\d+'  # Uninteresting: int
    re7='.*?'   # Non-greedy match on filler
    re8='(\\d+)'    # Integer Number 1

    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8,re.IGNORECASE|re.DOTALL)
    m = rg.search(txt)
    if m:
        attenValue=m.group(1)
        #print attenValue

	return attenValue

#writeAtten()

