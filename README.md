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



sub_filter '/web/' '/odoo/web/';
sub_filter '/mail/' '/odoo/mail/';
sub_filter '/web_enterprise/' '/odoo/web_enterprise/';
sub_filter '/bus/' '/odoo/bus/';
sub_filter '/base/static/' '/odoo/base/static/';
sub_filter '/base_setup/' '/odoo/base_setup/';
sub_filter '/base_import/' '/odoo/base_import/';
sub_filter '/website/translations' '/odoo/website/translations';
sub_filter '/qcent/' '/odoo/qcent/';
sub_filter 'href="/contactus"' 'href="/odoo/contactus"';
sub_filter 'href="/"' 'href="/odoo"';
sub_filter 'href="/web"' 'href="/odoo/web"';
sub_filter 'alt="Icon" src="/' 'alt="Icon" src="/odoo/';
sub_filter_once off;
sub_filter_types *;

