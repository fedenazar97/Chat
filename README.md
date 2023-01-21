# A simple social network with a real-time chat implemented with Django-channels

Is a full-stack application created with `Python-Django` and `HTML/CSS(Bootstrap)/JS(WebSockets)`

The application has user creation, login, changeof password, profile creation and update, chat in real-time.


Let's take a look at the app:

- Sign up:
    ![sign up](/images/SignUp.png)

- Log in:
    ![log in](/images/login.png)

- Personal profile update
    ![update profile](/images/UpdateProfile.png)

- Change of Password:
    ![cange password](/images/changePassword.png)

- Profiles created:
    ![profiles created](/images/ProfileList.png)

- Profile of another user and where you can start a chat:
    ![another user profile](/images/StartThread.png)

- My started chats:
    ![Mychats](/images/Mychats.png)

- Real time chat:
    ![chat](/images/chatFullscreen.png)
    ![chat2](/images/chatSplit.png)


# Installation to run locally
    
- In the terminal create and active your favorite virtual enviroment  

- Then, install the project's dependencies:
    ~~~
    pip install -r requirements.txt
    ~~~

- After that, migrate the app's models:
    ~~~
    python manage.py makemigrations
    ~~~
    and then :
    ~~~
    python manage.py migrate
    ~~~

- Start a Redis server on port 6379, run the following command:
    ~~~
    docker run -p 6379:6379 -d redis:5
    ~~~

- You can now run the server and enjoy.
    ~~~
    python manage.py runserver
    ~~~

## Future releases:

- Notifications for new messages.
- Dockerize and deploy.
