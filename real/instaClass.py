import json
import PIL.Image
import urllib
import urllib2

class instaClass:
    def __init__(self):
        pass

    def setUser(self, user):
        self.user = user

    def grabPhoto(self):
        response = urllib2.urlopen('https://www.instagram.com/'+self.user+'/?__a=1')
        data = json.load(response)

        self.url = data['user']['media']['nodes'][0]['display_src']
	self.width = data['user']['media']['nodes'][0]['dimensions']['width']
	self.height = data['user']['media']['nodes'][0]['dimensions']['height']

    def prepareUrl(self):
        self.savedUrl = self.url

        """Getting the high resolution instagram picture"""
        """self.url = self.url[7:]
        tmp1, tmp2 = self.url.split('/s640x640')
        self.url = tmp1 + tmp2"""
        self.url, garbage = self.url.split('?')

        self.current_url = self.url

    def savePhoto(self):
        """Grabs image from insta"""
        image = urllib.URLopener();
        image.retrieve(self.url, 'image.jpg');

        """Saves it to proper jpg"""
        PIL.Image.open('image.jpg').save('image.jpg', 'JPEG')

    def updatedPic(self):
        self.grabPhoto()
        if self.savedUrl is not self.url:
            return True

    def getHeight(self):
	return self.height

    def getWidth(self):
	return self.width
