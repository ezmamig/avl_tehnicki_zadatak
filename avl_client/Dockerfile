FROM python:alpine3.15
RUN pip install flask requests

WORKDIR /app
COPY ./avl_client .

EXPOSE 5000
ENV FLASK_APP=entrypoint.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]