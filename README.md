# Space Instagram  
Here you can find functions to fetch images from Hubble and Spacex websites using their API
 and post them to the instagram automatically.  
1.`fetch_hubble.py`  
2.`fetch_spacex.py`  
3.`instagram_image_posting_if.py` 

### 1.`fetch_hubble.py`   
This file is ready for use. By default it will download the picture with ID number `1` to the project file path which is
 `"Instagram_auto_posting/Space Pictures/"` and then it will thumbnail that picture to fit `Instagram`. 
 If you want the another picture , simply just change the `ID number`.
 
```python
IMAGE_ID = 1
FOLDER_PATH = 'Instagram_auto_posting/Space Pictures/' 
```

 You can also find some more useful information by going to the [Official Hubble API documentation](http://hubblesite.org/api/documentation).  
 As well as some more useful information can be found [over here](https://grantwinney.com/day-9-hubblesite-api/).
 
 ### 2.`fetch_spacex.py`    
This file basically does the same thing as a `fetch_hubble.py` 
 But instead of `image_id`, it takes `launch_number` as an argument.
 It can also take `"latest"` as an argument instead of number and it will get you the latest launch pictures.
 So by default this file will get you the latest launch pictures to the same project path `"Instagram_auto_posting/Space Pictures/"`
 
##### This is how will they appear in your folder  
 ```
SpaceX_flight pic 1.jpg
SpaceX_flight pic 2.jpg
SpaceX_flight pic 3.jpg
SpaceX_flight pic 4.jpg
SpaceX_flight pic 5.jpg
```
So the main difference between `fetch_hubble.py` and `fetch_spacex.py` is their API functionality.
`fetch_hubble.py` gives you only the one picture by its `id` and `fetch_spacex.py` gives you a set of pictures related to the particular launch.

[Here is API documentation](https://documenter.getpostman.com/view/2025350/RWaEzAiG?version=latest#bc65ba60-decf-4289-bb04-4ca9df01b9c1)  
[And here is Github SpaceX API repository](https://github.com/r-spacex/SpaceX-API)
 
 
 ### 3.`instagram_image_posting.py`  
 This function takes `folder_path` as an argument. So in this case it going to take pictures from the project folder
  `Instagram_auto_posting/Space Pictures/` and going to post them to your instagram one by one.  
  
### setting up .env variables   
  You will  have to set your environment variables up, with `.env` file where you going to store
  your `PASSWORD AND USERNAME`.  
  

  You can use [Notepad++](https://notepad-plus-plus.org/downloads/) to create this file for Windows,
or [CotEditor](https://coteditor.com/) for MacOS.
  
##### This is an example of how it looks like inside of your .env file. 
(You can choose your own variable names if you want)  
```
INSTAGRAM_USERNAME=YOURuserName
INSTAGRAM_PASSWORD=yOurPassWord

Variables has to be with CAPITAL letters and without any spaces at all!
```


More details about the Instagram Bot you can find [Here - Documentation for Developers](https://instagrambot.github.io/docs/en/For_developers.html#photos)   
and [Here - Github repository](https://github.com/instagrambot/instabot) 


## How to install  

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Project Goals  
To make life easier
