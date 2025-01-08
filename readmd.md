1. At first need to setup virtual environment: python -m venv task_env
2. Activate the environment: task_env/Scripts/activate
    - if you want to store versions of packages we used: pip freeze > requirements.txt
    - this help to copy the project: at new place you first need to setup new environment and activate then: pip install -r requirements.txt
3. Now, need to install Django at virual environment: pip install Django
    -> you can check pip list: will show Django at the list
4. Now, using Django we need to create a project: django-admin startproject task_management
Note: but this creates redundancy of same name folder. to ignore that use: django-admin startproject task_management .
5. Finally we can check the project is running or not: python manage.py runserver 

6. Now, for the project we may need to create app for each feature. For example here is the task management project initially we are planning to have two projects. tasks and users.
Create app: django-admin startapp tasks