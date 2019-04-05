package com.chyidl.tutorial;

public class ArithmeticOperationTest {

    public static void main(String[] args){
        /**
         * 算术运算符
         * */
        int a=10, b=20, c=25, d=25;
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("b / a = " + (b / a));
        System.out.println("b % a = " + (b % a));
        System.out.println("c % a = " + (c % a));
        System.out.println("a++   = " + (a++));
        System.out.println("a--   = " + (a--));
        // 查看d++ 与 ++d的不同
        System.out.println("d++   = " + (d++));
        System.out.println("++d   = " + (++d));

        /**
         * 关系运算符
         * */
        System.out.println("a == b = " + (a == b));
        System.out.println("a != b = " + (a != b));
        System.out.println("a > b = " + (a > b));
        System.out.println("a < b = " + (a < b));
        System.out.println("b >= a = " + (b >= a));
        System.out.println("b <= a = " + (b <= a));

        /**
         * 位运算符
         * */
        a = 60; /* 60 = 0011 1100 */
        b = 13; /* 13 = 0000 1101 */
        c = 0;
        c = a & b; /* 12 = 00001100 */
        System.out.println("a & b = " + c);

        c = a | b;  /* 61 = 0011 1101 */
        System.out.println("a | b = " + c);

        c = a ^ b; /* 49 = 0011 0001 */
        System.out.println("a ^ b = " + c);

        c = ~a; /* -61 = 1100 0011 */
        System.out.println("~a = " + c);

        c = a << 2; /* 240 = 1111 0000 */
        System.out.println("a << 2 = " + c);

        c = a >> 2; /* 15 = 0000 1111 */
        System.out.println("a >> 2 = " + c);

        c = a >>> 2; /* 15 = 0000 1111 */
        System.out.println("a >>> 2 = " + c);

        /**
         * 逻辑运算符
         * */
        boolean A = true;
        boolean B = false;
        System.out.println("A && B = " + (A && B));
        System.out.println("A || B = " + (A || B));
        System.out.println("!(A && B) = " + !(A && B));

        /**
         * 短路逻辑运算符
         * */
        int shortCircleA = 5; // 定义一个变量
        boolean shortCircleB = (shortCircleA < 4) && (shortCircleA++<10);
        System.out.println("使用短路逻辑匀速符的结果为" + shortCircleB);
        System.out.println("shortCircleA的结果为" + shortCircleA);

        /**
         * 赋值运算符
         * */
        a = 10;
        b = 20;
        c = 10;

        c = a + b;
        System.out.println("c = a + b = " + c);

        c += a;
        System.out.println("c += a = " + c);

        c -= a;
        System.out.println("c -= a = " + c);

        c *= a;
        System.out.println("c *= a = " + c);

        a = 10;
        c = 15;
        c /= a;
        System.out.println("c /= a = " + c);

        a = 10;
        c = 15;
        c %= a;
        System.out.println("c %= a = " + c);

        c <<= 2;
        System.out.println("c <<= 2 = " + c);

        c >>= 2;
        System.out.println("c >>= 2 = " + c);

        c &= a;
        System.out.println("c &= a = " + c);

        c ^= a;
        System.out.println("c ^= a = " + c);

        c |= a;
        System.out.println("c |= a = " + c);

        /**
         * 条件运算符
         * */
        a = 10;
        // 如果a等于1成立，则设置b为20,否则为30
        b = (a == 1) ? 20 : 30;
        System.out.println("Value of b is : " + b);

        // 如果a等于10成立,则设置b为20否则为30
        b = (a == 10) ? 20 : 30;
        System.out.println("Value of b is : " + b);

        /**
         * instanceof运算符
         * */
        String name = "ChyiYaqing";
        boolean result = name instanceof String; //

    }

}
