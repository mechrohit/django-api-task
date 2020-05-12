## To Run the Project locally Please follow the steps below
1. Clone the git repository 
2. Create the virtual environment
3. activate the virtual environment
4. Install required dependicies by running following commands : pip3 install -r requirements.txt
5. Go to the settings.py and comment out the line no 12 and line no 129 
   Line no 12  : import django_heroku
   Line no 129 : django_heroku.settings(locals())
6. Onces done run the below commands
   python manage.py migrate
   python manage.py createsuperuser [Enter the username, Email and Password]
   python manage.py runserver
7. Now go to the web url and enter the below url
   localhost:8000 and enter the username and password and test the below api
    "users": "http://localhost:8000/users/",
    "groups": "http://localhost:8000/groups/"
    
    
### Live Deployment [Heroku Server]
1. This project is deployed in Heroku server and below are the credentials
   Url: https://devina-django-api.herokuapp.com/
   Api for users details : https://devina-django-api.herokuapp.com/users
   Api for activity details : https://devina-django-api.herokuapp.com/groups
   
   Username : admin
   
   Password : admin
