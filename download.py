import requests
import sys

# 
arglist=sys.argv
def main():
 url=arglist[1]
 name=arglist[2]
# create a response object
 response=requests.get(url,stream=True)

# open a file
  
 with open(name,'wb') as nam :
	for chunk in response.iter_content(chunk_size=1024) :
	   if(chunk) :
		nam.write(chunk)

if __name__ == '__main__':
  main()
