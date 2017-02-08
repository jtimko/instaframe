import pygame
import time
import instaClass
import urllib2

url = urllib2.urlopen("http://www.renevario.com/id.php?id=143756")
user = url.read()
insta = instaClass.instaClass()
insta.setUser(user)

def gatherInfo():
    insta.grabPhoto()
    insta.prepareUrl()
    insta.savePhoto()


"""Setting up pygame"""
pygame.init()
size = width, height = 640, 640
black = 0,0,0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('Instagram Frame')
clock = pygame.time.Clock()

gatherInfo()
pic_height = insta.getHeight()
pic_width = insta.getWidth()

path = "image.jpg"
instapic = pygame.image.load(path)
instarect = instapic.get_rect()

done = False
while done is not True:
    screen.fill(black)
    rpic = pygame.transform.scale(instapic,(640, 640))
    rpic = pygame.transform.rotate(rpic, 90)
    screen.blit(rpic, (0,0))

    if insta.updatedPic() == True:
        gatherInfo()
        path = "image.jpg"
        instapic = pygame.image.load(path)
        instarect = instapic.get_rect()
    url = urllib2.urlopen("http://www.renevario.com/id.php?id=143756")
    user = url.read()
    insta.setUser(user)

    pygame.display.flip()
    time.sleep(30)
