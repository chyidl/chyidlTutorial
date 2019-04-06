package com.chyidl.tutorial;

import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils;
import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.io.*;

/**
 * Java Stream 流， File文件， IO
 * */
public class FileStreamIOTest {

    public static void main(String[] args) {

        /**
         * 读取控制台输入
         * */
        char c = '-';
        String str = "-";
        // 使用 System.in 创建 BufferedReader
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        System.out.println("Enter lines of text.");
        System.out.println("Enter 'end' to quit.");
        // readLine() 读取字符串
        do {
            try{
                str = br.readLine();
                System.out.println(str);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }while (!str.equals("end"));
        System.out.println("输入字符，按下'q'键推出.");
        // read() 读取字符
        do {
            try {
                c = (char) br.read();
            } catch (IOException e) {
                e.printStackTrace();
            }
            System.out.println(c);
        } while (c != 'q');

        // 演示 System.out.write()
        int b = 'A';
        System.out.write(b);
        System.out.write('\n');

        /**
         * 读写文件
         * FileInputStream : 从文件中读取数据
         * FileOutputStream: 创建一个文件并向文件中写数据
         * */
        try{
            byte[] bWrite = {11, 21, 3, 40, 5};
            OutputStream os = new FileOutputStream("test.txt");
            for (int x =0; x < bWrite.length; x++){
                os.write(bWrite[x]); // writes the bytes
            }
            os.close();

            InputStream is = new FileInputStream("test.txt");
            int size = is.available();
            for (int i=0; i<size; i++){
                System.out.println((char) is.read() + " ");
            }
            is.close();
        }catch (IOException e) {
            e.printStackTrace();
        }

        try {
            File f = new File("a.txt");
            FileOutputStream fop = new FileOutputStream(f);
            // 构建FileOutputStream对象，文件不存在会自动新建

            OutputStreamWriter writer = new OutputStreamWriter(fop, "UTF-8");
            // 构建OutputStreamWriter对象，参数可以指定编码，默认为操作系统默认编码，window是GBK

            writer.append("中文输入");
            // 写入缓冲区

            writer.append("\r\n");
            // 换行

            writer.append("English");
            // 刷新缓存区，写入到文件，如果下面已经没有写入的内容，直接close也会写入

            writer.close();
            // 关闭写入流，同时会把缓冲区内容写入文件

            fop.close();
            // 关闭输出流，释放系统资源

            FileInputStream fip = new FileInputStream(f);
            // 构建FileInputStream对象

            InputStreamReader reader = new InputStreamReader(fip, "UTF-8");
            // 构建InputStreamReader对象，编码与写入相同

            StringBuffer sb = new StringBuffer();
            while (reader.ready()) {
                sb.append((char) reader.read());
                // 转成char加到StringBuffer对象中
            }
            System.out.println(sb.toString());
            reader.close();
            // 关闭读取流

            fip.close();
            // 关闭输入流，释放系统资源
        } catch (IOException e) {
            e.printStackTrace();
        }

        /**
         * 创建目录
         *  mkdir() 方法创建一个文件夹
         *  mkdirs()方法创建一个文件夹和它的所有父文件夹
         * */
        String dirname = "/Users/chyiyaqing/chyidl.com/chyidlTutorial/root/java/javaTutorial/javaIdea/test";
        File d = new File(dirname);

        // 现在创建目录
        d.mkdirs();

        //读取目录
        dirname = "/Users/chyiyaqing";
        File f1 = new File(dirname);
        if (f1.isDirectory()){
            System.out.println("目录 " + dirname);
            String s[] = f1.list();
            for (int i = 0; i < s.length; i++) {
                File f = new File(dirname + "/" + s[i]);
                if (f.isDirectory()) {
                    System.out.println(s[i] + " 是一个目录");
                } else {
                    System.out.println(s[i] + " 是一个文件");
                }
            }
        } else {
            System.out.println(dirname + " 不是一个目录");
        }

    }
}
