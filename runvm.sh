python="$(which python)"
pip="$(which pip)"

[ ! -d "venv" ] && echo "Directory venv DOES NOT exists." && $python -m virtualenv venv || source venv/bin/activate
$pip install -r requirements.txt
$python website/manage.py makemigrations
$python website/manage.py migrate
$python website/manage.py runserver
