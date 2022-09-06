from PIL import Image 
from urllib import request
import os
import requests
import configparser

bearer_token = ''
user_name = ''

def read_config():
    config = configparser.ConfigParser()
    config.read('circle.conf')
    keys = [
        "bearer_token",
        "twitter_user_name"
    ]
    for key in keys:
        try:
            value = config.get("SETTINGS", key)
        except configparser.NoOptionError:
            print(f"No option '{key}' in section 'SETTINGS'")
            return False
    
    global bearer_token
    bearer_token  = config.get("SETTINGS", "bearer_token")
    global user_name
    user_name  = config.get("SETTINGS", "twitter_user_name")
    return True


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def create_url():    
    url = "https://api.twitter.com/2/users/by/username/{}?{}".format(user_name, 'user.fields=id,profile_image_url')
    return url


def create_search_url(userid):    
    url = "https://api.twitter.com/2/users/{}/mentions?max_results=100&expansions=author_id&user.fields=id,username,profile_image_url".format(userid)
    return url


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )
    return response


def main():
    if not read_config():
        exit('Missing config variable')
    ImageSize = 400

    url = create_url()
    response = connect_to_endpoint(url) 
    json_response = response.json()    
    userid = json_response['data']['id']
    profile_image_url = json_response['data']['profile_image_url']
    url = create_search_url(userid)
    response = connect_to_endpoint(url) 
    json_response = response.json()   

    mention = {}
    for dataset in json_response['data']:
        if not dataset['author_id'] in mention:
            mention[dataset['author_id']] = 1
        else:
            mention[dataset['author_id']] = mention[dataset['author_id']] + 1

    sorted_mention = sorted(mention.items(), key=lambda kv: kv[1])
    sorted_mention.reverse()

    index = 1
    for m in sorted_mention:
        if index <= 8:
            for u in json_response['includes']['users']:
                if u['id']==m[0]:
                    url = u['profile_image_url']
                    url = url.replace("normal.jpg", "400x400.jpg")
                    request.urlretrieve(url,'{}.jpg'.format(index))
        index = index + 1
        
            
        
    MainImage = Image.new('RGB',[ImageSize,ImageSize],int('000000', 16))
    profile_image_url = profile_image_url.replace("normal.jpg", "400x400.jpg")
    request.urlretrieve(profile_image_url,'user.jpg')
    TWImage = Image.open('user.jpg').resize([128,128])
    BGImage = Image.open('bg.jpg').resize([128,128])
    MaskImage = Image.open('mask.png').resize([128,128])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2), int((ImageSize - UserImage.height) / 2)))
    os.remove('user.jpg')

    TWImage = Image.open('1.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2), int((ImageSize - UserImage.height) / 2) - 128))
    os.remove('1.jpg')

    TWImage = Image.open('2.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2) + 100, int((ImageSize - UserImage.height) / 2) - 100))
    os.remove('2.jpg')

    TWImage = Image.open('3.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2) + 128, int((ImageSize - UserImage.height) / 2)))
    os.remove('3.jpg')

    TWImage = Image.open('4.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2) + 100, int((ImageSize - UserImage.height) / 2) + 100))
    os.remove('4.jpg')

    TWImage = Image.open('5.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2), int((ImageSize - UserImage.height) / 2) + 128))
    os.remove('5.jpg')

    TWImage = Image.open('6.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2) - 100, int((ImageSize - UserImage.height) / 2) + 100))
    os.remove('6.jpg')

    TWImage = Image.open('7.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2) - 128, int((ImageSize - UserImage.height) / 2)))
    os.remove('7.jpg')

    TWImage = Image.open('8.jpg').resize([80,80])
    BGImage = Image.open('bg.jpg').resize([80,80])
    MaskImage = Image.open('mask.png').resize([80,80])
    UserImage = Image.composite(TWImage,BGImage,MaskImage)
    MainImage.paste(UserImage, (int((ImageSize - UserImage.width) / 2) - 100, int((ImageSize - UserImage.height) / 2) - 100))
    os.remove('8.jpg')

    MainImage.save('export/circle.jpg')
    


if __name__ == "__main__":
    main()