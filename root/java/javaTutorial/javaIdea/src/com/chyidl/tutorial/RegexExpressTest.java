package com.chyidl.tutorial;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.StreamSupport;

/**
 * Java 正则表达式
 * Java.util.regex 主要包括一下三类
 *      Pattern 类：编译表示
 *      Matcher 类：是对输入字符串进行解释和匹配操作的引擎
 *      PatternSyntaxException: 是一个非强制异常类，表示一个正则表达式模式中的语法错误
 * Java中，\\代表其他语言中的一个\,\\\\表示一个普通的反斜杠
 * 正则表达式可以用来搜索、编辑或处理文本
 * 正则表达式不仅仅限于某一种语言，但是每种语言中有细微的差别
 *  \   : 下一字符标记为特殊字符
 *  ^   :  匹配输入字符串开始的位置
 *  $   : 匹配输入字符串结尾的位置
 *  *   : 零次或多次匹配前面的字符或子表达式
 *  +   ：一次或多次匹配前面的字符或子表达式
 *  ?   : 零次或一次匹配前面的字符或子表达式
 *  {n} : 匹配n次
 *  {n,}    : 至少匹配n次
 *  {n,m}   : 至少匹配n次，至多匹配m次
 *  ?   : 当此字符紧随其他限定符之后时，匹配模式是非贪心匹配，非贪心匹配模式匹配搜索尽可能短的字符串，默认贪心模式匹配搜索到尽可能长的字符串
 *  .   : 匹配除\r\n之外的任何单个字符，若要匹配包括\r\n在内的任意字符，请使用\s\S之类的模式
 *  {pattern}: 匹配pattern并捕获匹配的子表达式，若要匹配括号()请使用\(,\)
 *  {?:pattern}: 匹配pattern但不捕获该匹配的子表达式，即它是一个非捕获匹配，不存储
 *  {?=pattern}: 正向预测先行搜索的子表达式
 *  {?!pattern}: 反向预测先行搜索的子表达式
 *  x|y : 匹配x或y
 *  [xyz]: 匹配包含的任一字符
 *  [^xyz]:反向字符集，匹配未包含的任意字符
 *  [a-z]: 字符范围，匹配指定范围内的任何字符
 *  [^a-z]: 反向范围字符，匹配不在指定的范围内的任何字符
 *  \b: 匹配一个字边界，即字与空格间的位置
 *  \B: 非字边界匹配
 *  \cx: 匹配x指示的控制字符
 *  \d: 数字字符匹配，等效[0-9]
 *  \D: 非数字字符匹配,
 *  \f：换页符匹配
 *  \n:换行符匹配
 *  \r:匹配一个会车符
 *  \s:匹配任何空白字符
 *  \S:匹配任何非空白字符
 *  \t:制表符匹配
 *  \v:垂直制表符匹配
 *  \w:匹配任何字类字符
 *  \W:任何非单词字符匹配
 *  \xn:匹配n,此处的n是一个十六进制的转义码，例如: "\x41" 匹配A
 *  \num:匹配num,此处的num是一个正整数，
 *  \n:标示一个八进制转义码或反向引用，
 *  \nm:
 * */
public class RegexExpressTest {
    public static void main(String[] args) {
        String content = "I am noob " + "from runoob.com";
        String pattern = ".*runoob.*";

        boolean isMatch = Pattern.matches(pattern, content);
        System.out.println("字符串中是否包含了 'runoob' 子字符串? " + isMatch);

        // 按指定模式在字符串查找
        String line = "This order was placed for QT3000! OK?";
        pattern = "(\\D*)(\\d+)(.*)"; // \\表示一个正则表达式的反斜线，所以其后的字符具有特殊意义

        // 创建 Pattern对象
        Pattern r = Pattern.compile(pattern);

        // 现在创建matcher对象
        Matcher m = r.matcher(line);
        if (m.find()){
            System.out.println("Found value: " + m.group(0));
            System.out.println("Found value: " + m.group(1));
            System.out.println("Found value: " + m.group(2));
            System.out.println("Found value: " + m.group(3));
        } else {
            System.out.println("NO MATCH");
        }

        final String REGEX = "\\bcat\\b";
        final String INPUT = "cat cat cat cattie cat";

        Pattern p = Pattern.compile(REGEX);
        m = p.matcher(INPUT); // 获取matcher对象
        int count = 0;

        // find() 尝试查找与该模式匹配的输入序列的下一个子序列
        while(m.find()){
            count++;
            System.out.println("Match number " + count);
            System.out.println("start(): " + m.start()); // 返回以前匹配的初始索引
            System.out.println("end(): " + m.end()); // 返回最后匹配字符之后的偏移量
        }

        /**
         * matches 和 lookingAt
         *  matches要求整个序列都匹配
         *  lookingAt不要求整个序列都匹配
         * */

        final String REGEX2 = "foo";
        String INPUT2 = "foooooooooooooooooo";
        String INPUT3 = "ooooofooooooooooooo";
        Pattern pattern2 = Pattern.compile(REGEX2);
        Matcher matcher2 = pattern2.matcher(INPUT2);
        Matcher matcher3 = pattern2.matcher(INPUT3);

        System.out.println("Current REGEX is: " +REGEX2);
        System.out.println("Current INPUT is: " +INPUT2);
        System.out.println("Current INPUT2 is: " + INPUT3);
        System.out.println("lookingAt(): " + matcher2.lookingAt());
        System.out.println("matches(): " + matcher2.matches());
        System.out.println("lookingAt(): " + matcher3.lookingAt());

        /**
         * replaceFirst 和 replaceAll
         * */
        String REGEX3 = "dog";
        INPUT3 = "The dog says meow. " + "All dogs say emow.";
        String REPLACE = "cat";

        p = Pattern.compile(REGEX3);
        // get a matcher object
        m = p.matcher(INPUT3);
        INPUT3 = m.replaceAll(REPLACE);
        System.out.println(INPUT3);


    }
}
