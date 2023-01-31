rm -rf $(find . -name migrations )
./manage.py makemigrations main
./manage.py makemigrations
./manage.py migrate
