export SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://bless:123@localhost/blog"
export MAIL_USERNAME='loisemuthoni181@gmail.com'
export MAIL_PASSWORD='0725408650'
export SECRET_KEY ='JHGVBN'

python3 manage.py server
# python3 manage.py shell

# python manage.py db init
# python manage.py db migrate -m "Initial Migration"
# python manage.py db upgrade
