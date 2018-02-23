# smart-content
Content and User Management for Smart Contract


**System Setup**

1. Python Setup
    We support Python 3.6+. To check your current version, `python3 --version`
    To install Python 3.6+, use following steps:
    
    * If on Ubuntu 16.04 or older, `sudo add-apt-repository ppa:deadsnakes/ppa`. Else, skip this step
    * `sudo apt-get update`
    * `sudo apt-get install python3.6`


**Repo Setup**

1. Clone the git repo locally.

1. Environment Setup

    * Create a new Virtual Environment.
        * Make sure this virtual environment is using Python 3 and Associated Pip
        * For pip3, use following: `wget https://bootstrap.pypa.io/get-pip.py`, `sudo python3.6 get-pip.py`, `sudo pip3.6 install virtualenv`
        * Get Virtualenv wrapper (if not already existing in system): `sudo apt-get install virtualenvwrapper` 
        * To then associate Python Version with virtualenv, we use: `mkvirtualenv -p /usr/bin/python3.6 <virtualenv_name>`
        
    * Install the requirements.
           `pip install -r requirements.txt`

    * Create '.env' file in project root directory to override any environment variables.
          * To override the settings file use
             `DJANGO_SETTINGS_MODULE=mcloud.settings.local`

1. Configuration setup

    * Create local setting by copying local.py.template file to local.py.
    * Update all settings as necessary

1. Run Migrations

    * Run `python manage.py migrate`

1. Run server on local

    * Run `python manage.py runserver <port>`. Note: default port is `8000`
