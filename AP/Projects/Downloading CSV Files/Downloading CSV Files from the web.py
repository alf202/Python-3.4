#Modules to import
from urllib import request

#The CSV to download
goog_url = 'http://payneslan.co.uk/csv.csv'

#Connecting,download and storing the file
def download_stock_data(csv_url):
    response =  request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)