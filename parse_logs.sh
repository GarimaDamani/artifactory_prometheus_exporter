#!/bin/bash/

FILE_PATH=”/var/opt/scripts/past_1min.log”
FETCH_LOG=”/var/opt/jfrog/artifactory/logs/request.log”

while true
do
    TIME=$(date — date “-1min” ‘+%Y%m%d%H%M’)
    sed -n “/^$TIME/,$ p” $FETCH_LOG > $FILE_PATH
    echo -n “$(grep ‘HTTP/1.1|20.|’ $FILE_PATH | wc -l)” > /var/opt/scripts/parse.out.log
    echo -n “ $(grep ‘HTTP/1.1|40.|’ $FILE_PATH | wc -l)” >> /var/opt/scripts/parse.out.log
    echo -n “ $(grep ‘HTTP/1.1|50.|’ $FILE_PATH | wc -l)” >> /var/opt/scripts/parse.out.log
    echo -n “ $(grep ‘|GET|’ $FILE_PATH | wc -l)” >> /var/opt/scripts/parse.out.log
    echo -n “ $(grep ‘|PUT|’ $FILE_PATH | wc -l)” >> /var/opt/scripts/parse.out.log
    sleep 60
done
