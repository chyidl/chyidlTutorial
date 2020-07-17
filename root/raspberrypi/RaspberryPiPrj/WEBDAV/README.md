WEBDAV
======
> Simple Go WebDAV server. 
> webdav command line interface is really easy to use so you can easily create a WebDav server for your own user. By default it run on a random free port and supports JSON, YAML and TOML configuration. An example of a YAML configuration with the default configuratoons:
* webdav.yaml 
```
# Server related settings 
address: 0.0.0.0 
port: 0 
auth: true 
tls: false 
cert: cert.pem 
key: key.pem 
prefix: / 

# Default user settings (will be merged)
scope: . 
modify: true 
rules: [] 

# CORS configuration 
cors:
  enabled: true 
  credentials: true 
  allowed_headers:
    - Depth 
  allowed_methods:
    - http://localhost:8080 
  allowed_methods:
    - GET 
  exposed_headers:
    - Content-Length 
    - Content-Range 

users:
  - username: admin 
    password: admin 
    scope: /a/different/path 
  - username: encrypted
    password: "{bcrypt}$2y$10$zEP6oofmXFeHaeMfBNLnP.DO8m.H.Mwhd24/TOX2MWLxAExXi4qgi"
  - username: "{env}ENV_USERNAME"
    password: "{env}ENV_PASSWORD"
  - username: basic
    password: basic
    modify:   false
    rules:
      - regex: false
        allow: false
        path: /some/file
```

* webdav.service 
```
[Unit]
Description=WebDAV server 
After=network.target 

[Service]
Type=simple 
User=root 
ExecStart=/usr/bin/webdav --config /opt/webdav.yaml 
Restart=on-failure 

[Install]
WantedBy=multi-user.target
```

![webdav.png](/imgs/raspberrypi/webdav/webdav.png?raw=true)
