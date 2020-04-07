Provisioning a new site
============================

## Required Packages

nginx
Python 3.6
virtualenv + pip
Git

##Nginx Virtual Host config
see nginx.template.conf
replace DOMAIN with domain of website

##Systemd service
see gunicorn-systemd.template.service
replace DOMAIN with domain of website

Assume we have a user account at /home/username

/home/username
|______(whatever you use for sites)
  |______DOMAIN1
  |   |____.env
  |   |____db.sqlite3
  |   |____manage.py etc
  |   |____static
  |   |____virtualenv
  |______DOMAIN2
      |____.env
      |____db.sqlite3
      |____etc
