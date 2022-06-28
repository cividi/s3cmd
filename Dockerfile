FROM alpine:latest
MAINTAINER cividi

RUN apk add --no-cache python3 py-pip py-setuptools git ca-certificates

RUN pip install python-magic \
  && git clone https://github.com/s3tools/s3cmd.git /tmp/s3cmd \
  && cd /tmp/s3cmd \
  && python3 /tmp/s3cmd/setup.py install \
  && cd / \
  && rm -rf /tmp/s3cmd \
  && apk del py-pip git

COPY run.py /run.py
COPY crontab.txt /crontab.txt
COPY entry.sh /entry.sh
COPY .s3/.s3cfg /root/.s3cfg

RUN chmod 755 /entry.sh

WORKDIR /s3

# ENTRYPOINT ["s3cmd"]
CMD ["/entry.sh"]
