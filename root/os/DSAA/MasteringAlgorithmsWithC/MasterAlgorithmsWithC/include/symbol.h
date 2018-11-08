//
//  symbol.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for a Simple Lexical Analyzer 
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef symbol_h
#define symbol_h

/**
 * 模拟输入流拆分函数
 * 
 * @param istream 输入流
 *
 * @return 标记 (NULL 表示结束)
 * */
static char *next_token(const char *istream)
{
    return NULL;
}

/**
 * 符号标记
 * */
typedef struct {
    char    *lexeme;
    Token   token;

} Symbol;


#endif /* symbol_h */
