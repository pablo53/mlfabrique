FROM python:3.7

COPY requirements.txt /
RUN pip install -r requirements.txt
RUN useradd --no-create-home --user-group mlfadmin
RUN mkdir -p /opt/mlfabrique/nnloader
RUN chmod -R a+r,a+w,a+x /opt/mlfabrique
USER mlfadmin
COPY *.py /opt/mlfabrique/nnloader

EXPOSE 5000
WORKDIR /opt/mlfabrique/nnloader
ENTRYPOINT FLASK_APP=restloader.py flask run --host=0.0.0.0
