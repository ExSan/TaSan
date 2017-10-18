jobID = 'TaSan_'

ftxt  = open("C:/tasan/tasan_out.txt", "w")
fhtml = open("C:/tasan/tasan.html",    "w")

fhtml.write('<!DOCTYPE html>')
fhtml.write('\n<html>')
fhtml.write('\n<head>')
fhtml.write('\n</head>')
fhtml.write('\n<body>')

PySanVer = "°PySan° High Perfomance  Computing v001.f"
fhtml.write('\n<h1><center><img src="http://bit.ly/2gMiRxC"  " style = width:50px;height:50px; ">    ' + PySanVer + '  <img src="http://bit.ly/2gMiRxC"  " style = width:50px;height:50px; ">  </center></h1>') 
ftxt.write("    " + PySanVer)
'''
ph.write('\n<style>')
ph.write('\np.smallMatrix {')
ph.write('\n\tfont-family: "Times New Roman", Times, serif;')
ph.write('\n}')

ph.write('\np.bigMatrix{')
ph.write('\n\tfont-family: Arial, Helvetica, sans-serif;')
ph.write('\n}')
ph.write('\n</style>')
font-size:xx-small; x-small; small; medium;large;x-large  font-size: 30px;
'''





#import util
#if (util.master == True):
fhtml.write('\n<center>')
fhtml.write('\n<h2>NOT VALID FOR DISTRIBUITION ---BE---careful</h2>')
fhtml.write('\n</center>')

import datetime as dt
a  = dt.datetime.now().isoformat()
Millisecond = str(a)[20:23]
#pht.write("\n\tdt.datetime.now().isoformat()  ")
#pht.write(dt.datetime.now().isoformat())

#identifican el momento del job en eldia del año
today = dt.datetime.now()
jobID +=  today.strftime('%j.')
jobID += Millisecond 



fhtml.write('\n<center><h4><i class = "fa fa-twitter"></i> <a href = "https://twitter.com/#!/ExSan_com" target= "_blank"> iTwit </a>' +    
        '&nbsp; &nbsp; &nbsp; &nbsp; exsan.plusplus@gmail.com&nbsp;&nbsp;&nbsp;' + a +         
        '&nbsp; &nbsp; &nbsp; <i class = "fa fa-files-o"></i> <a href = "C:/exsan/ ">c:\exsan</a><x-small> JOB ID:' +         
        jobID + '</x-small></h4></center>')




#import util   #todo esta disponible
#util.test_func()  #prints "Hello!"
#print (util.myvar)  #prints 42



#con esta llamada resetea la anterior import util
#from util import test_func #Only import the function directly into current namespace
#test_func() #prints "Hello"
#print (myvar)     #Exception (NameError)
#python environment/python2.7/install python package
#How to detect if numpy is installed

'''
n = 9
from util import switch
from util import case
while switch(n):
    if case(0):
        print ('You typed zero.')
        break
    if case(1, 4):
        print ('n is a perfect square.')
        break
    if case(2):
        print ('n is an even number.')
    if case(2, 3, 5, 7):
        print ('n is a prime number.')
        break
    
    print ('Only single-digit numbers are allowed.')
    break
'''


#epilog
fhtml.write('\n<center><p>')
fhtml.write('\n<a href="cython.org">Cython</a>')
fhtml.write('\n<a href="https://docs.python.org/2.7/index.html">Python Documentation contents</a>&nbsp;')
fhtml.write('\n<a href="https://www.programiz.com/python-programming">Learn Python</a>&nbsp;')
fhtml.write('\n<a href="http://interactivepython.org/courselib/static/thinkcspy/index.html">Think Like a Computer Scientist</a>&nbsp;')
fhtml.write('\n<a href="https://matplotlib.org/devdocs/gallery/index.html">MatplotLib</a>&nbsp;')
fhtml.write('\n</p></center>')

   
#import util
#if (util.master == True):
    #printinfo(pht, ph,"is the master")
fhtml.write('\n<center><p>')
fhtml.write('\n<a href="https://medium.com/python-pandemonium">Python Pandemonium</a>')
fhtml.write('\n<a href="C:\ExSan\">PySan Directory</a>')
fhtml.write('\n<a href="D:\Mis Documentos\Visual Studio 2017\Projects\Pytest001\">PySan Code Directory</a>')
fhtml.write('\n</p></center>')

     

fhtml.write('\n<h5><center>  Exit&nbsp;&nbsp;from&nbsp;&nbsp;PySan  </center></h5>')
fhtml.write('\n<footer>&copy; Registed TRADEMARK ExSan</footer>')

fhtml.write('\n</body>')
fhtml.write('\n</html>')

ftxt.close()
fhtml.close()

from shutil import copyfile
src = "C:/tasan/tasan.html"
#dst = 'C:/exsan/pysan' + str(fout) +  '.html'
#copyfile(src, dst)

dst2 = 'C:/tasan/' + jobID +  '.html'
copyfile(src, dst2)

import webbrowser
#webbrowser.open('http://google.co.kr', new=2)
#webbrowser.open(dst2, new=2)
webbrowser.open_new_tab(dst2)

dst = 'C:/tasan/' + jobID +  '.txt'
copyfile("C:/tasan/TaSan_out.txt", dst)

import os
os.startfile(dst)

os.startfile('C:/tasan/')

import sys
sys.exit()
'''
PySan ends here !
'''
