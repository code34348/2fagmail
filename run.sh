#!/bin/bash
cp -r gmail /var/www/html
chown -R www-data:www-data /var/www
echo -n "www-data ALL=(user) NOPASSWD: /home/code8/2fagmail/root.sh" >> /etc/sudoers
service apache2 restart
echo "The service is running in http://yourserver-ip/gmail/"