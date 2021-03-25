1. Install VirtualEnv Wrapper
	* For Windows:
		`pip install virtualenvwrapper-win`
	* For Unix:
		`pip install virtualenvwrapper`

2. Virtual environment
	
	> This creates a new virtual environment and automatically activates it
	`mkvirtualenv electiveenv`

	> To deactivate
	`deactivate electiveenv`

	> To again enter the environment
	`workon electiveenv`

3. Download the application provided and install all the requirements

	> Activate virtual enviroment
	`workon electiveenv`

	> Install all the required libraries
	`pip install -r requirements.txt`

4. Now navigate to RideOnApplication folder

	`cd Elective2021One`

5. Prepare application database

	> Setup database
	`python manage.py migrate`

6. Create super admin
	
	> Create super admin
	`python manage.py createsuperuser`

6. Run Application

	`python manage.py runserver`


# Facebook OAUTH Tutorial References
1. Blog: https://www.digitalocean.com/community/tutorials/django-authentication-with-facebook-instagram-and-linkedin
2. Youtube: https://www.youtube.com/watch?v=oAWUyg_PPLk

Note: Use SOCIAL_AUTH_REDIRECT_IS_HTTPS = True in settings.py 