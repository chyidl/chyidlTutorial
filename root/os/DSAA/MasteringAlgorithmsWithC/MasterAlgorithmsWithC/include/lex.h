//
//  lex.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for a Simple Lexical Analyzer 
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef lex_h
#define lex_h

#include "chtbl.h"

/*************************************************
 * Define the token recognized by the lexical analyzer.
 * **********************************************/
typedef enum Token_ {lexit, error, digit, other} Token; 

/********************************************************
 * Public Interface 
 * *****************************************************/

/**
 * 根据输入流生成符号表
 *
 * @param istream 输入流
 * @param symbol 符号表
 *
 * @return 类型
 * */
Token lex(const char *istream, CHTbl *symtbl);


#endif /* lex_h */
