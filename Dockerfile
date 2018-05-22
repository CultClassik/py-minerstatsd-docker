FROM: library/python:3.6.5

LABEL "maintainer"="Chris Diehl <cultclassik@gmail.com>"

COPY app/* /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["/app/app.py"]
CMD [ "--interval", "20", "--url", "http://localhost:3333" ]

# run 1 of these containers per gpu
# each minestatsd will export stats from ethminer/claymore via http api to the hosts' collectd daemon
# interval and url will be passed as params to the container on run
#  the url should be the name of the gpu mining container to be monitored
