# Award
A web app that enables user to post their projects and get rated based on design, usability and content.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

# Prerequisites
What things you need to install the software and how to install them

Django and Python Needed<br>
First you need to clone this project to your local machine

      git clone https://github.com/Developer-Gitonga/Awards.git<br>
# Installing
First we install virtualenv and activate it<br>
To install it run the command

         python3 -m venv env

After the installation is done, now its time to activate the env

         source env/bin/activate

Next we need to install all the requirements for the project from the requirements.txt file

         pip3 install -r requirements.txt

Now its time to run the code

         python3 manage.py runserver
        
 # Extra
To use my api navigate to this urls

To retrieve user profile data

         awwards-dev-git.herokuapp.com/api/profiles/
To retrieve all the projects

         awwards-dev-git.herokuapp.com/api/projects/
         
# Built With
Python - The language mostly used<br>
Django - The framework used<br>
Cloudinary - Used for image upload<br>
Heroku - Used for deployment<br>
Contact details<br>
Email: aizensalim@@gmail.com

# MIT licence
Copyright (c) 2022 Moringa School

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
