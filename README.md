
	
# Add-text-banner-to-video 
Videos with some text around it makes more impact than a normal video, it helps you to understand context better. Such videos are trending on social media a lot and apparently there is no open source tool or code I could find to make such videos. So this simple python-OpenCV code will add text banner around any video.  
It takes input video, text to be written and logo as input and generate text added video as output. 
 
 
Installation steps: 
 
If you are a handy user of python and hopefully have python installed on your windows then, just install OpenCV, moviepy and numpy libraries to make this code work. 
 
If you do not have python installed in your system and you consider yourself a beginner please follow these steps : 
 
Step 1: Download Anaconda for windows from here (https://www.continuum.io/downloads#windows) 
Choose 64-bit or 32-bit according to your system configuration. When it comes to choosing between python 2.7 and 3.6, I personally recommend 3.6. 
Now just get it installed, this video can help you through it (https://www.youtube.com/watch?v=SjKtDEEv0_E). 
 
Step 2: create an environment to work on and activate it. Open command prompt and type this command  
        conda create --name work 
        activate work 
 
Step 3: Now install ffmpeg, OpenCV and Moviepy libraries in your working environment. Type these commands one by one on command prompt
        conda install -c conda-forge ffmpeg=3.2.4 
        conda install -c conda-forge opencv=3.2.0 
        pip install moviepy (if this does not work try->  sudo pip install moviepy) 
 
Step 4: Copy all the files and code to your system. Go to the directory in command prompt, where you want this code to be saved and then run these commands 
	conda install git	
	git clone https://github.com/MayankSharma-MS/Add-text-banner-to-video.git

Now you are all set to run the code. Type this command on cmd prompt
	python addTextBannerToVideo.py

You can use your own input videos, text, font size and watermark by changing values in addTextBannerToVideo.py file.
