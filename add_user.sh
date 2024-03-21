#!/bin/bash

URL="http://localhost:8080/ocs/v1.php/cloud/users"
USERNAME="Gaiiaalessio"
PASSWORD="Admin"
PASSWORD_ENCODED="abc123abc!" 


for i in {1..30}; do
    USERID="user$i"
    docker exec -i -u 33 gaialessio-app-1 bash -c "export OC_PASS=$PASSWORD_ENCODED && /var/www/html/occ user:add $USERID --password-from-env"
done
