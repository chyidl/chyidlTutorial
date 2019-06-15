/*
 * MyServletA.java
 * Servlets
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/15/19 07:49.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.io.*;
// import two of the servlet packages
import javax.servlet.*;
import javax.servlet.http.*;

/**
 * Most 'normal' servlets will extend HttpServlet, 
 * then override one or more methods
 * */
public class MyServletA extends HttpServlet {
    
    /**
     * Override the doGet for simple Http Get message 
     * @param request: the client request 
     * @param response: the server send back response
     * */
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // This tell the sever what kind of 'thing' is 
        // coming back from the server as a result of this servlet running
        response.setContentType("text/html");
        
        // The response object gives us an output stream to 'write' information back out to the server 
        PrintWriter out = response.getWriter();

        // What we 'write' is an HTTP page! 
        String message = "If you're reading this, it worked!";
        out.println("<HTML><BODY>");
        out.println("<H1>" + message + "</H1>");
        out.println("</BODY></HTML>");
        out.close();
    }
}

