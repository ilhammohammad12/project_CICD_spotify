From python
Workdir /app
COPY . . 
Run pip install -r requirements.txt
Expose 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]