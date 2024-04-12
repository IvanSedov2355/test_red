FROM python:3.9
COPY ./backend /app
WORKDIR /app
ENV PYTHONPATH=/app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
#CMD ["gunicorn", "app.stocks_products.wsgi:aplication", "--bind", "0.0.0.0:8000"]
EXPOSE 5000
CMD python3 backend.py
