# todo_project/settings.py

INSTALLED_APPS = [
    ...
    'todo_app', # Make sure your app is added here
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # This creates the file in your main folder
    }
}
