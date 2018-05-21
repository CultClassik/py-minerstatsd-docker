FROM: library/python:3.6.5-onbuild

LABEL "maintainer"="Chris Diehl <cultclassik@gmail.com>"

COPY app/* /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# map your own private ssh key here as readonly
VOLUME /key.rsa

EXPOSE 8000

#CMD [ "pypy3", "/app/app.py" ]
#CMD ["gunicorn", "app:api", "--name", "r10kdeploy", "--bind", "0.0.0.0:8000"]
CMD [ 'app.py', '--interval', '20', '--url', 'http://localhost:3333' ]

# run 1 of these containers per gpu
# each minestatsd will export stats from ethminer/claymore via http api to the hosts' collectd daemon
# interval and url will be passed as params to the container on run
#  the url should be the name of the gpu mining container to be monitored
