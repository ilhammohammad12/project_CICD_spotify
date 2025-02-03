From python
Workdir /app
COPY . . 
Run pip install -r requirements.txt
Expose 8000
#CMD ["python","spotify/manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "spotify.wsgi:application"]
