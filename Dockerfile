FROM python:3.9
WORKDIR /ipfs-cdn/
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 80
ENTRYPOINT gunicorn app:app -c gunicorn.py