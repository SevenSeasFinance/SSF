export DEBUG=1
export HOST="8.213.20.43"

# FOR DATABASE CONNECTIONS WITH POSTGRE
export DATABASE_NAME="TEST"
export DATABASE_USER="Test"
export DATABASE_PASS="Aa1234567!"
export DATABASE_HOST="pgm-l4vuo37wo3bcmv8m217630.pgsql.me-central-1.rds.aliyuncs.com"
export DATABASE_PORT="5432"

# FOR S3
export OSS_ACCESS_KEY_ID="LTAI5t8xMjEJ7pfudCqkbxt3"
export OSS_ACCESS_KEY_SECRET="4stoy0N3jvYlqV1xlyj75eYvl9NxPV"
export OSS_EXPIRE_TIME="2592000"
export OSS_BUCKET_NAME="test-hello-world-ssf"
export OSS_ENDPOINT="oss-me-central-1.aliyuncs.com"

apt-get update && apt-get upgrade
apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx -y

# pip install virtualenv
# Change the name django oss backend from force_text to force_str
pip install django django-oss-storage psycopg2
pip install -r requirements.txt


sed -i 's/force_text/force_str/g' /usr/local/lib/python3.10/dist-packages/django_oss_storage/backends.py
python3 SSF/manage.py makemigrations main
python3 SSF/manage.py makemigrations
python3 SSF/manage.py migrate
python3 SSF/manage.py runserver 0.0.0.0:8000
