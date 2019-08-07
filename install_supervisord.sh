# Installing Supervisord

apt-get update && apt-get install -y python-setuptools
easy_install supervisor
mkdir /etc/supervisor
echo_supervisord_conf >  /etc/supervisor/supervisord.conf
mkdir /etc/supervisor/conf.d
