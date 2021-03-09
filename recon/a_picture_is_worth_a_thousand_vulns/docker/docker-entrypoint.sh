#!/bin/bash

chown -R www-data:www-data /var/www/html/
chmod -R 777 /var/www/html/
service apache2 start

exec "$@"

while true; do
    sleep 1000
done