#14-7-2017 NLTK, corpora ... Swadehs list ... different languages
#import nltk
#nltk.download()
#from nltk.corpus import swadesh
# Todor Arnaudov playing

# -*- coding: utf-8 -*-
from nltk.corpus import swadesh
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

#import sys, locale, os
#print(sys.stdout.encoding)
#print(sys.stdout.isatty())
#print(locale.getpreferredencoding())
#print(sys.getfilesystemencoding())
#print(os.environ["PYTHONIOENCODING"])
#print(chr(246), chr(9786), chr(9787))

j=0
f = open("sw.txt", "wb")

length = [207, 207, 207, 207, 207, 174, 207, 207 ]
top = 0
all = 0

for i in swadesh.words(): 
  s = str(j) + "-" + str(j%length[top])
  
  #s = str(j)
  #f.write( (s+": " + i + "\r\n").encode('utf-8')); j+=1
  f.write((i+ "\r\n").encode('utf-8')); j+=1
  all = all+1
  #if (all == length[top]): all = 0; top+=1
f.close()
#from nltk.corpus import swadesh