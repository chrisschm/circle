from PIL import Image 
from urllib import request
import os
import requests

ImageSize = 200

MainImage = Image.new('RGB',[ImageSize,ImageSize],int('000000', 16))


#ausgabetext = "Der Preis für 2 Socken beträgt 5 DM und 5 Paar kosten 10 DM"
#print(ausgabetext)
#ausgabetext = ausgabetext.replace("DM", "Euro")

#ausgabetext = ausgabetext.replace("normal.jpg", "400x400.jpg")



request.urlretrieve('https://pbs.twimg.com/profile_images/1484957634864287746/8ZsvSwVY_400x400.jpg','user.jpg')

TWImage = Image.open('user.jpg').resize([64,64])
BGImage = Image.open('bg.jpg').resize([64,64])
MaskImage = Image.open('mask.png').resize([64,64])

UserImage = Image.composite(TWImage,BGImage,MaskImage)



MainImage.paste(UserImage, (int((ImageSize - UserImage.height) / 2), int((ImageSize - UserImage.width) / 2)))


MainImage.save('export/circle.jpg')
os.remove('user.jpg')