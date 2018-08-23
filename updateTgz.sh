#!/bin/sh
#pushd /data/tars_deploy/ && git pull && popd
#rm -rf /data/Tars/tars_deploy
#cp -rf /data/tars_deploy/ /data/Tars/
\cp -r /data/Tars_add/tars*/  /data/Tars/cpp/framework/deploy/
\cp -rf /data/Tars_add/db/*  /data/Tars/cpp/framework/sql
mkdir -p /usr/local/app/
rm -rf /data/Tars/web
cp -rf /data/Tars_add/web /data/Tars/web

