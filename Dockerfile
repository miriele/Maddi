FROM python:3.8

# /media 폴더를 Docker volume에 연결합니다.
VOLUME ["/media"]

COPY . .

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
