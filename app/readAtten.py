#!/usr/bin/python

import telnetlib
import re

from __main__ import *

def readAtten1():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA1\n')
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
        atten1=m.group(1)
        #print atten1
        return atten1

def readAtten2():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA2\n')
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
        atten2=m.group(1)
        #print atten2
        return atten2

def readAtten3():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA3\n')
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
        atten3=m.group(1)
        #print atten3
        return atten3

def readAtten4():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA4\n')
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
        atten4=m.group(1)
        #print atten4
        return atten4

def readAtten5():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA5\n')
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
        atten5=m.group(1)
        #print atten5
        return atten5

def readAtten6():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA6\n')
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
        atten6=m.group(1)
        #print atten6
        return atten6

def readAtten7():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA7\n')
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
        atten7=m.group(1)
        #print atten7
        return atten7

def readAtten8():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA8\n')
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
        atten8=m.group(1)
        #print atten8
        return atten8

def readAtten9():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA9\n')
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
        atten9=m.group(1)
        #print atten9
        return atten9

def readAtten10():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA10\n')
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
        atten10=m.group(1)
        #print atten10
        return atten10

def readAtten11():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA11\n')
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
        atten11=m.group(1)
        #print  atten11
        return atten11

def readAtten12():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA12\n')
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
        atten12=m.group(1)
        #print atten12
        return atten12

def readAtten13():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA13\n')
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
        atten13=m.group(1)
        #print atten13
        return atten13

def readAtten14():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA14\n')
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
        atten14=m.group(1)
        #print atten14
        return atten14

def readAtten15():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA15\n')
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
        atten15=m.group(1)
        #print atten15
        return atten15

def readAtten16():
    
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RA16\n')
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
        atten16=m.group(1)
        #print atten16
        return atten16

