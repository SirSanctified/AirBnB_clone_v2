#!/usr/bin/env bash
# set up web servers for deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
  Welcome to AirBnB clone
  </body>
</html>" >> /data/web_static/releases/test/index.html
ln -f --symbolic "/data/web_static/releases/test/" "/data/web_static/current"
chown --recursive ubuntu:ubuntu "/data/"
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart


