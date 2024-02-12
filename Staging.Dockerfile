FROM httpd:2.4

COPY --chown=www-data:www-data _site /usr/local/apache2/htdocs/