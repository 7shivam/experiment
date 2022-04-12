FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./backend /app/backend
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","src.index:app","--host=0.0.0.0","--reload"]
