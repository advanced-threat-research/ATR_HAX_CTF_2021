FROM bitbull/webserver-dev:php5.6

ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ADD index.html .
ADD check_answers.php .
ADD range_extender.png .
EXPOSE 80
ENTRYPOINT ["/docker-entrypoint.sh"]
