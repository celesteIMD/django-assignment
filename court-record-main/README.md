# Instructions to set up and run my app 

Hello! Welcome to my app. I am assuming Python, Git, and PyCharm have been installed on your computer.

**Run this command before doing anything else:** `git config --global core.editor "nano"` 

1) Open a terminal and navigate to the folder you want to create your project in (e.g. `cd ~Documents/Code`)
2) Clone this repository with `git clone <link to this repository>`
3) Open the repository with PyCharm. You can do this by going file->open and selecting the cloned folder called `project-celesteIMD`. You may need to log in with your git account to access it. 
4) Open a terminal using PyCharm and install dependencies using `pip install -r requirements.txt`
5) Create a file called `.env` in the top level directory (should be in the same folder as manage.py)
6)  Generate a secret key by running `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` in the terminal. Copy the output.
7) Edit `.env` (created in part 5) and add a line that says `SECRET_KEY="your-secret-key-here"`. Paste the output from part 6 into 'your-secret-key-here'.
8) On the terminal, run 'python -m pip install Pillow'. If it tells you that Pillow isn't installed when you try to run the app, and then says Pillow IS installed when you try to install it in a paradoxical loop, please try quitting PyCharm and reopening it again (that fixed it for me!).
9) On the terminal, run `python manage.py migrate`
10) Run the server by clicking the play button or running `python manage.py runserver` on the terminal
11) Navigate to 127.0.0.1:8000!
12) Create a user account with python manage.py createsuperuser
13) Log in on the browser with the user account you just made
14) Type in /admin after the url to access admin controls. Add a few users (fill in text fields for username, password, and password confirmation). Add a few pieces of evidence (fill in text fields for title, description, category, a selection drop down for LegalUser, and upload a photo (multimedia!!) for icon). And finally, add a few Battles (fill in number field for year, text field for verdict, and select one or more users for legalUsers). Or you can add to the database using the site itself! Everything is (hopefully!) working at this point.

Now everything should hopefully be set up! :D 
