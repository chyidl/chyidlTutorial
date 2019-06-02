curl - transfer a URL
=====================
> curl is a tool to transfer data from or to a server, uring one of the supported protocols (DICT,FILE,FTP,FTPS,GOPHER,HTTP,HTTPS,IMAP,IMAPS,LDAP,LDAPS,POP3,POP3S,RTMP,RTSP,SCP,SFTP,SMB,SMBS,SMTP,SMTPS,TELNET and TFTP).

> curl offers a busload of useful tricks like proxy support, user authentication, FTP upload, HTTP post, SSL connections, cookies, file transfer resume, Metalink, and more.

```
Verbose
$ curl -v http://www.example.com/

Output
curl outputs the response body to standard output.
$ curl -o out.json http://www.example.com/index.html

GET
the default method when making HTTP calls with curl.
$ curl -v http://101.71.156.153:9997/quote/v1/real?en_prod_code=688992.SS 

POST
$ curl -d 'user=haha&password=passwd' http://localhost:8082/spring-rest/ 

```
