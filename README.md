**Introduction**

This directory contains image-scraping software, which allows you to download all **available** images from the Favorites folder of any Flickr user.


**Requirements**

Python 3.9 or later with all of the pip install -U -r requirements.txt packages including:

    flickrapi

    requests

**Install**

$ git clone https://github.com/Annyvk/Flickr_Favorites_Image_Scraper

$ pip install -U -r requirements.txt

**Run**

1. Request a Flickr API key: https://www.flickr.com/services/apps/create/apply

2. Write your API key and secret in Flickr_favorites.py L5-L6:

    KEY = ''

    SECRET = ''

3. Write ID of the user whose Favorite images you want to download in Flickr_favorites.py L7:

    USER_ID = ''

You can find out the user ID from the url.
For example:

    https://www.flickr.com/photos/67370113@N02/
    "67370113@N02" is user ID.

4. Write a folder path where you want to save the images in Flickr_favorites.py L45, L46, L4

5. All images size is "Medium" (800x800) by default. To get original size images, change the 'url_c' parameter to 'url_o' in Flickr_favorites.py L31, L36.
