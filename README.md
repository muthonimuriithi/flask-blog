# PERSONAL-BLOG

##### By Loise Muthoni 

## Table of Content

+ [Description](#description)
+ [Installation Requirement](#Installation)
+ [Technology Used](#technology-used)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#author-Info)

## Description

This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. with a feature that displays random quotes to inspire your users.


## Installation and setup

To view the app, open the live site link provided below on the README. Here is a run through of how to set up the application:

* Here is the live link to the blog: https://bloggbless.herokuapp.com/ 

1. Clone this repository using git clone: or downloading a ZIP file of the code.https://github.com/muthonimuriithi/flask-blog.git

2. The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened

3. Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:

pip install virtualenv, virtualenv env, source env/bin/activate

Note that you can exit the virtual environment by running the command deactivate

4. Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL databse client.

5. Download the all dependencies in the requirements.txt using pip install -r requirements.txt
Create a file in your root directory called start.sh and store a generated SECRET key like so export SECRET_KEY="<your-key>"

On the same file write down the command python3 manage.py server
Step 6 : On your terminal, run the following command, chmod a+x start.sh
You can now launch the application locally by running the command ./start.sh

### Behavior Driven Development

* INPUT
1. Subscribe to mail list, Input the email	Redirect you to the index page.
2. Writer login, Take you to home page, redirects you to the Homepage
3. Create a blog post by filling blog form	Write your blog and post it to blog, your blog is       displayed in index page
3. User comment on the Blog post plus a nickname, write your feedback and post it, your feedback is displayed under the blog post
4. Writer delete a blog post, deleting the blog post from the database, the blog post will be deleted and not appear on the page
5. Writer update a blog post, updating the blog post in database, the blog post will be updated
6. Writer delete a comment, deleting the blog post in database, the comment will no longer appear under the post






## Technology Used

* Python3
* Flask
* Javascript
* Particle Js
* Html5
* Css3
* Bootstrap4

## User Story

1. User can view the blog posts on the site
2. User sees random quotes on the site
3. User can view the most recent posts
4. User can subscribe to blog mailing list and receives an email alert when a new post is made.
5. User can comment on blog posts

## Writer view

1.sign in to the blog.
2. create a blog from the application,
delete comments that I find insulting or degrading
update or delete blogs I have created.


## Licence

MIT License

Copyright (c) [2022] [Loise Muthoni]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Authors Info
For any inquires please email me at

Email : loissmuthoni@student.moringaschool.com

Email: loisemuthoni181@gmail.com
