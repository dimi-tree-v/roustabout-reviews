./venv/Scripts/activate.bat & ^
set DJANGO_SETTINGS_MODULE=base.settings & ^
cd roustabout_reviews & ^
python manage.py migrate & ^
# python manage.py makemigrations --check --dry-run & ^
python manage.py runserver localhost:8000
