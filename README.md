This is code for automating the repositary creation in git and github.

READ CAREFULLY

NOTE:
# You should have git bash to run the command (git command work only if git bash is installed).
# Also you should have chrome and download the web driver for it. https://chromedriver.chromium.org/downloads
# Download for your version of chrome.(To find your chrome version, go to help [will be inside the three dots on top right corner], then about google chrome. There you will find the version) 

SETUP:
# Go to the web driver downloaded folder.
# Extract it and move the .exe file to c:\Program files(x86)
# Create a new folder named "github" in c:\User\user_name\documents
# Then go into the .py file and put your github username (Email) and github password on line 24 and 29 respectively.  
# 
Move the .bat file into C:\wiindows\system32 folder and run this command on command line (cmd or any terminal) to create the repositary
  create-repo your_repositary_name

The code will open the browser and signin and create a repositary.
It will also clone the repositary with the readme file to your local machine.
