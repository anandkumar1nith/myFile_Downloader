import requests

url="http://www.axmag.com/download/pdfurl-guide.pdf"
# create a response object
response=requests.get(url,stream=True)

# open a file
  
with open("a.pdf",'wb') as pdf :
	for chunk in response.iter_content(chunk_size=1024) :
	   if(chunk) :
		pdf.write(chunk)
