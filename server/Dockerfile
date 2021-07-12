FROM alpine:3.12.4

ENTRYPOINT ["/bin/bash", "/home/euvsc/entrypoint.sh"]
WORKDIR /home/euvsc

RUN apk add bash curl python3 py3-pip 

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

RUN addgroup -S euvsc && \
    adduser -s /bin/bash -G euvsc -S euvsc && \
    (echo euvsc ; echo euvsc) | passwd euvsc

COPY --chown=euvsc:euvsc \
     static \
     /home/euvsc/static/

COPY --chown=euvsc:euvsc \
     templates \
     /home/euvsc/templates/

COPY --chown=euvsc:euvsc \
     vsu_server.py \
     entrypoint.sh \
     /home/euvsc/

USER euvsc
