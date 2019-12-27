import urllib.request

print('Beginning file download with urllib2...')

url = 'http://212.68.57.202/images/B23072019_V1_K1/frame0.jpg'
urllib.request.urlretrieve(url, '/Users/batuhanbayraktar/PycharmProjects/Savasan-IHA-Fighter-UAV/photosForAI/frame0.jpg')
