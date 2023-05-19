Conda:
conda create -n Djangofr python==3.11
conda create --name $ENVIRONMENT_NAME python
conda activate $ENVIRONMENT_NAME*
conda deactivate
conda list --name $ENVIRONMENT_NAME
conda info —envs
conda install python=x.x
conda list —export
Conda remove “env_name”
conda clean
conda remove -n Djangof —all
django-admin --version
django-admin startproject E_commerce_Project
cd E_commerce_Project
python manage.py runserver
python manage.py startapp Login_App
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
from Login_App.models import Student
s1 = Student(name = 'Joe', course = 'a', city = 't', college = 'd', email = '@gm')
s1.name
S1.save()

——
Static files - images, css, JS
Templates - HTML file
