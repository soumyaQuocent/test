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



location ~* \.(woff2|css|js|gif|png|jpg|jpeg|svg)$ {
        add_header Cache-Control "public, max-age=31536000, immutable";
        expires 365d;
    }
