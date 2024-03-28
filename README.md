Some cookies are misusing the recommended “SameSite“ attribute 4
GET https://tmsinfostagging.adani.com/web/static/src/libs/fontawesome/fonts/fontawesome-webfont.woff2?v=4.7.0 [HTTP/1.1 404 Not Found 10ms]

GET https://tmsinfostagging.adani.com/web/assets/455-dcd24e2/1/web.assets_frontend.min.css [HTTP/1.1 404 Not Found 30ms]

GET https://tmsinfostagging.adani.com/web/assets/200-f57b172/1/web.assets_frontend_minimal.min.js [HTTP/1.1 404 Not Found 27ms]

GET https://tmsinfostagging.adani.com/web/assets/200-f57b172/1/web.assets_frontend_minimal.min.js [HTTP/1.1 404 Not Found 3ms]

Loading failed for the <script> with source “https://tmsinfostagging.adani.com/web/assets/200-f57b172/1/web.assets_frontend_minimal.min.js”. odoo:42:198
GET https://tmsinfostagging.adani.com/web/image/website/1/favicon?unique=e427355 [HTTP/1.1 404 Not Found 4ms]

GET https://tmsinfostagging.adani.com/web/image/website/1/logo/Adani TMS Staging?unique=e427355 [HTTP/1.1 404 Not Found 4ms]

GET https://tmsinfostagging.adani.com/web/static/img/odoo_logo_tiny.png [HTTP/1.1 404 Not Found 10ms]

The resource at “https://tmsinfostagging.adani.com/web/static/src/libs/fontawesome/fonts/fontawesome-webfont.woff2?v=4.7.0” preloaded with link preload was not used within a few seconds. Make sure all attributes of the preload tag are set correctly.

[Checked]

location ~* \.(woff2|css|js|gif|png|jpg|jpeg|svg)$ {
        add_header Cache-Control "public, max-age=31536000, immutable";
        expires 365d;
    }



    location /web {
        proxy_pass http://odoo;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location /mail {
        proxy_pass http://odoo;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
location / {
        rewrite ^/(.*)/static/description/(.*)$ /odoo/$1/static/description/$2 last;
    }

[To be Check]
        Modify the command to include the --dev flag: Simply add --dev at the end of your startup command. For example, if your original command is ./odoo-bin -c odoo.conf, it would become ./odoo-bin -c odoo.conf --dev.

        ./odoo-bin -c odoo.conf --dev -u all




location ~ ^/(?<module_name>[^/]+)/static/description/(?<icon>.+)$ {
        rewrite ^ /odoo/$module_name/static/description/$icon last;
    }

https://tmsinfostagging.adani.com/odoo/web#cids=1&action=menu



logger.info('**************************************')
logger.info('domain_from',domain_from)
logger.info('**************************************')
logger.info('domain_to',domain_to)

