import requests
import sys

def main():
 url=sys.argv[1
# create a response object
 response=requests.get(url,stream=True)

# open a file
  
 with open("a.pdf",'wb') as pdf :
	for chunk in response.iter_content(chunk_size=1024) :
	   if(chunk) :
		pdf.write(chunk)
