# OPTIONAL ZSH and Oh My ZSH
```
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

# Pyenv
```
sudo apt-get update; 
sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
curl https://pyenv.run | bash
```

### Add to .zshrc or .bashrc 
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

# Install nginx, postgres and rabbitmq
```
sudo apt-get install nginx                    
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install rabbitmq-server              
sudo apt-get install libpq-dev   
```

# Nginx
- create a config similar to the one in nginx_configs and mv it to `/etc/nginx/sites-available/` 
- link site 
`sudo ln /etc/nginx/sites-enabled/<name_of_my_site> /etc/nginx/sites-available/<name_of_my_site>`
- start nginx
`sudo systemctl start nginx`
 
# Create user in database for django to use
- In postgres creating a user will need to be lower case, if you create user API it will create it as api
```
sudo -u postgres -i
psql
CREATE DATABASE <db_name>;
CREATE USER <username> with PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE <dn_name> TO <user>;
ALTER DATABASE <db_name> OWNER TO <user>
GRANT CREATE ON SCHEMA public TO <user>;
exit
```
# create a user in rabbitmq for celery app and virtual host
```
sudo rabbitmqctl add_user <user> <password>
sudo rabbitmqctl set_user_tags <user> <tag>
sudo rabbitmqctl add_vhost <name_for_virtual_host>
sudo rabbitmqctl set_permissions -p <name_for_virtual_host> <user> ".*" ".*" ".*"
```


# Setting up ubuntu desktop (Optional)
```
sudo apt-get install ubuntu-desktop gnome-shell-extension-prefs gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal tigervnc-standalone-server gnome-panel gnome-tweaks gnome-shell-extension-ubuntu-dock gnome-software gedit
vim ~/.vnc/xstartup
sudo reboot
```

# Create virtual env for Python Django project
- install python version and create virtual env
```
pyenv install -list  # shows all verions that can be installed
pyenv install <VERSION_OF_PYTHON>
pyenv virtualenv <VERSION_OF_PYTHON> <NAME_OF_VIRTUAL_ENV>
```
- move to directory where you will want project to be
`pyenv local <NAME_OF_VIRTUAL_ENV>

- Install dependecies from requirements.txt
```
pip install --upgrade pip
pip install -r requirements.txt
```

- start project and application for django
```
django-admin startproject <PROJECT_NAME>
cd <PROJECT_NAME>
python manage.py startapp <APPLICATION_NAME>
```

- collectstatic and move it to /etc/nginx/
```
sudo python manage.py collectstatic
```

- update setting.py in PROJECT_NAME directory with database credentials
- update celery app with rabbitmq credentials

# Create Gunicorn service
- modify the gunicorn service file in the services directory, then cp it to `/etc/systemd/system/gunicorn.service` 
- modify the gunicorn socket file in the services directory, the cp it to `/etc/systemd/system/gunicorn.socket`
- start gunicorn service
```
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
```

# Create Celery service
- modify the celery service file in the services directory then cp it to `/etc/systemd/system/celery.service`
```
sudo systemctl enable celery
sudo systemctl start celery
```

