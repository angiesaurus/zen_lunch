pkill -f manage.py
sleep 2
./manage.py runfcgi host=127.0.0.1 port=8080