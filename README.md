This is code for automating the repositary creation in git and github.

**READ CAREFULLY**

**NOTE:**
1. You should have git bash to run the command (git command work only if git bash is installed).
2. Also you should have chrome and download the web driver for it. https://chromedriver.chromium.org/downloads
3. Download for your version of chrome.(To find your chrome version, go to help [will be inside the three dots on top right corner], then about google chrome. There you will find the version) 

**SETUP:**
1. Go to the web driver downloaded folder.
2. Extract it and move the .exe file to c:\Program files(x86)
3. Create a new folder named "github" in c:\User\user_name\documents
4. Then go into the .py file and put your github username (Email) and github password on line 25 and 30 respectively.  
5. Move the .bat file into C:\wiindows\system32 folder and run this command on command line (cmd or any terminal) to create the repositary
  
  create-repo your_repositary_name

The code will open the browser and signin and create a repositary.
It will also clone the repositary with the readme file to your local machine.
