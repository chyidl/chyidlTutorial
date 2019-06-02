/*
 * DailyAdviceClient.java
 * chap15
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/28/19 11:00.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.io.*;
import java.net.*;

public class DailyAdviceClient {

    public void go() {
        try {
            /**
             * Make a socket connection to whatever is running on port 4242
             * on the same host this code is running on. (The 'localhost')
             * */
            Socket s = new Socket("127.0.0.1", 4242);

            InputStreamReader streamReader = new InputStreamReader(s.getInputStream());
            BufferedReader reader = new BufferedReader(streamReader);

            String advice = reader.readLine();
            System.out.println("Today you should: " + advice);

            // this close All the streams
            reader.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public static void main(String[] args)
    {
        DailyAdviceClient client = new DailyAdviceClient();
        client.go();
    }
}

