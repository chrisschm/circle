from PIL import Image 
from urllib import request
import os

ImageSize = 200

MainImage = Image.new('RGB',[ImageSize,ImageSize],int('000000', 16))


request.urlretrieve('https://pbs.twimg.com/profile_images/1484957634864287746/8ZsvSwVY_400x400.jpg','user.jpg')

TWImage = Image.open('user.jpg').resize([64,64])
BGImage = Image.open('bg.jpg').resize([64,64])
MaskImage = Image.open('mask.png').resize([64,64])

UserImage = Image.composite(TWImage,BGImage,MaskImage)



MainImage.paste(UserImage, (int((ImageSize - UserImage.height) / 2), int((ImageSize - UserImage.width) / 2)))


MainImage.save('export/circle.jpg')
os.remove('user.jpg')