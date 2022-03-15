FROM python:3.9
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
ENTRYPOINT ["gunicorn", "app:app", "-c", "gunicorn.py"]