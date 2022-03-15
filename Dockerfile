FROM python:3.9
WORKDIR /ipfs-cdn/
COPY . .
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
EXPOSE 80
ENTRYPOINT gunicorn app:app -c gunicorn.py