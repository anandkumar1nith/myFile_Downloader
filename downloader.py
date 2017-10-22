import urllib2

#
url="http://www.axmag.com/download/pdfurl-guide.pdf"

response=urllib2.urlopen(url)
meta=response.info()
# file name and file size
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
 downloaded=r"downloaded %10d percent"%((complete*100/file_size))
 print downloaded

file_.close()
 

