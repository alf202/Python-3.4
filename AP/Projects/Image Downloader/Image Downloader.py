import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://hackingwidsri.files.wordpress.com/2015/08/127-0-0-1-local-host-photos1.jpg")

