/*The stdio.h header defines three variable types, several macros, and various functions for performing input and outpyt.*/
#include <stdio.h>
/*The stdlib.h header defines four variable types several macros, and various functions fro performing general functions.*/
#include <stdlib.h>
/*sys/socket.h - Internet Protocol family*/
#include <sys/socket.h>
/*netinet/in.h - Internet address family*/
#include <netinet/in.h>

int make_socket (uint16_t port) 
{
    int sock;
    struct sockaddr_in name;

    /* 创建字节流类型的 IPv4 socket. */
    sock = socket(PF_INET, SOCK_STREAM, 0);
    if (sock < 0)
    {
        perror ("socket");
        exit (EXIT_FAILURE);
    }
    
    /*绑定到port 和 ip*/
    name.sin_family = AF_INET; /* IPV4*/
    name.sin_port = htons (port);   /*制定端口*/
    name.sin_addr.s_addr = htonl (INADDR_ANY); /*通配地址*/
    /*把 IPv4地址转换成通用地址格式，同时传递长度*/
    if (bind (sock, (struct sockaddr *) &name, sizeof (name)) < 0)
    {
        perror ("bind");
        exit (EXIT_FAILURE);
    }
    return sock;
}
