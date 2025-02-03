From Python:3.9-slim
Workdir /app
COPY . . 
Run pip install -r requirements.txt
Expose 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]