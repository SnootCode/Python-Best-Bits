# 
# Example file for retrieving data from the internet
#

import urllib.request # Make http requests

def main():
  webUrl = urllib.request.urlopen("http://www.theDBCX.com")
  print("result code: " + str(webUrl.getcode())) # code = 200, everything okay / 404, error
  data = webUrl.read()
  print(data)

if __name__ == "__main__":
  main()
