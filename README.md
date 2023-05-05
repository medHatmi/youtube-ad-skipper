README file for YouTube Ad Skipper

This script uses Selenium WebDriver to automate the process of skipping YouTube ads. It works by locating the "Skip Ad" button on YouTube videos and clicking it automatically.

Prerequisites
This script requires the following packages to be installed:

Selenium WebDriver
webdriver_manager
ChromeDriver (Automatically installed using webdriver_manager)
Usage
Install the required packages using pip install -r requirements.txt.
Run the script using python ad_skipper.py.
The script will open a Chrome window and navigate to YouTube.
The script will automatically skip ads on videos.
How it works
The script uses Selenium WebDriver to automate the process of skipping YouTube ads. It locates the "Skip Ad" button on videos and clicks it automatically. The script waits for the button to appear using WebDriverWait, and clicks it using driver.execute_script().

The script is set to run continuously until it is manually stopped. If there are no ads to skip, it waits for 3 seconds before checking again.

Disclaimer
Please use this script responsibly and at your own risk. Skipping ads may violate YouTube's terms of service or the terms of service of individual content creators.



