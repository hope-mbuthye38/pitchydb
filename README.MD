## Author
Hope Mbuthye
 # Features
As a user of the application, you will be able to:

See different pitches posetd by other people
Post your own pitch
Vote for other people's posts
Comment on other people's pitches
create an account, login and update your profile
 # BDD
Behaviour	input	output
View all pitches	Home page displays all pitches	Home page displays all pitches
login	Click on login	allows user to login into the account using the login form
create an account	Click on sign in	form which allos users to sign in for the first time
post a pitch	Click on Post pitch	brings an input form for posting a pitch
vote for a pitch	Click on upvote/downvote	The number of upvotes and downvotes increacres by one
comment on a post	Click on comment	Display a comment box to allow users to post a comment on a specific pitch
Update profile	Click on Profile	Takes the user to the profile page with options to edit and upload profile picture
Getting started
# Prerequisites
python
Virtual environment
pip
 # Cloning
Navigate into the folder you want the application to be In your terminal, run the commands

$ git clone https://github.com/hope-mbuthye38/pitchydb.git

$ cd PitchApp

 # Running the application
Modify the start.sh file with your own api key
To run the app type the commands in your terminal install all the dependencies listed in the requirements.txt file
$ chmod a+x start.sh

$ ./start.sh

Testing the application
To run the tests for the class in your terminal
$ python3.6 manage.py test

Technologies used
Python Flask Html Bootstrap

Known Bugs
The gmail server port specified is not responding which means the welcome email is not sent

# License
This project is Licensed under MIT. ©2019 Copyright.

# Collaborate
To Collaborate, Reach me out at:

# Github: 
hope-mbuthye38
# license
mit licence copyright @ Hope Mbuthye