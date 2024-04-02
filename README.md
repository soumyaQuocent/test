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




location ~ ^/(?<module_name>[^/]+)/static/description/(?<icon>.+)$ {
        rewrite ^ /odoo/$module_name/static/description/$icon last;
    }

https://tmsinfostagging.adani.com/odoo/web#cids=1&action=menu

[02/Apr/24]

logger.info('**************************************')
logger.info('domain_from',domain_from)
logger.info('**************************************')
logger.info('domain_to',domain_to)

