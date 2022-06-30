import flickrapi
import requests
import os

KEY = '...'  # Enter your API_KEY
SECRET = '...'  # Enter your Secret
USER_ID = '...'  # Enter User_id user's Favorites you need

flickr = flickrapi.FlickrAPI(api_key=KEY, secret=SECRET, format='parsed-json', cache=True)


def get_favorites_photos_info():
    favorites_photos_info = flickr.favorites.getList(user_id=USER_ID,
                                                     page=1,
                                                     per_page=500,
                                                     )
    total_pages = favorites_photos_info['photos']['pages']  # Total quantity pages in Favorites
    return total_pages


def get_favorites_photos_urls():
    total_pages = get_favorites_photos_info()
    photo_urls = []  # List of URLs of available images that are in the Favorites
    photo_id = []  # List of image IDs in Favorites whose URLs cannot be accessed
    photo_urls_count = 0

    for page_number in range(1, total_pages):
        favorites_photos = flickr.favorites.getList(user_id=USER_ID,
                                                    page=page_number,
                                                    per_page=500,
                                                    extras='url_c'
                                                    )

        for photo_urls_count in range(0, len(favorites_photos['photos']['photo'])):
            try:
                photo_urls.append(favorites_photos['photos']['photo'][photo_urls_count]['url_c'])
            except KeyError:
                photo_id.append(favorites_photos['photos']['photo'][photo_urls_count]['id'])
            photo_urls_count = photo_urls_count + 1
    return photo_urls


def get_favorites_photos():  # Downloading images from the list of received urls
    photo_urls = get_favorites_photos_urls()
    if not os.path.exists('Enter your folder path'):  # Checking the existence of a folder with this name
        os.mkdir('Enter your folder path')  # Creating a folder
    for photos_count in range(0, len(photo_urls)):
        img_data = requests.get(photo_urls[photos_count]).content
        with open(f'Enter your folder path/image_name_{photos_count}.jpg', 'wb') as file:
            file.write(img_data)


get_favorites_photos()
