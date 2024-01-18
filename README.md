local test superuser:
username: stunning_moments_superuser
password: stunningpass3

username: cloudy_pilot_user
password: cloudypass3

username: isabella
password: isapass3

username: isabella2
password: isapass32


Elephant superuser:
username: superusertest1
password: ?

username: testuser3
password: testpass3

username: testuser32
password: testpass32

To add users to local test, comment out `os.environ['DEV'] = '1'`, uncomment to store on ElephantSQL

Default images for profile picture and images are provided by Code Institute.
Every image in this API are hosted and stored using Cloudinary, and Pillow

There are details that won't be pushed to the main branch, in order to make the neccessary details work, this command was run in the terminal: `pip3 freeze > requirements.txt`

The following command was entered in the terminal to begin setup the Django rest framework:
`pip3 install djangorestframework`
Next, added to the installed apps list

for each change to the libraries, such as imports, it's neccessary to make a freeze

Switching to another platform:
In case you need to switch platform, for instance, Codeanywhere to VS code, make sure to run this command in the terminal:
`pip3 install -r requirements.txt`

Whitenoise:
During deployment for Heroku, the API may look differently. Although its function isn't lost, it may be nice to have the API look nice when you visit. Whitenoise attempt to fix that.
whitnoise `pip3 install whitenoise`
This API haven't yet successfully installed it. Here's a resource to resume that: https://www.w3schools.com/django/django_static_whitenoise.php

In case of Bad request 400:
 A common cause is disallowed host. Check if the deployed link is listed.