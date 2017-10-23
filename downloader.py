import urllib2
import sys

arglist=sys.argv
#
url=arglist[1]

response=urllib2.urlopen(url)
meta=response.info()
# file name and file size
if len(url.split('/')[-1])>50 :
 file_name="abc"
else :
 file_name=url.split('/')[-1]



file_size=int(meta.getheader('content-length')[0])


# u se hame read karna hai and f mai write karna hai



file_=open(file_name,'wb')


complete=0
chunk_size=1024

block=response.read(chunk_size)

while len(block)>0 :
 file_.write(block)
 complete+=len(block)
 block=response.read(chunk_size)
 downloaded=r"downloaded %10d Mb of %10d Mb"%((complete/10000,file_size))
 print downloaded

file_.close()
 
