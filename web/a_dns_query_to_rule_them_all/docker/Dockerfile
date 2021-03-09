FROM bitbull/webserver-dev:php5.6

ADD index.html .
ADD dns_get.php .
ADD flag.txt .
RUN /bin/bash -c 'apt-get update && apt-get -y install dnsutils'
EXPOSE 80
