//
//  lex.c
//  MasterAlgorithmsWithC
//  Descripted -- the Chained Hash Table
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#include "lex.h"
#include "chtbl.h"
#include "symbol.h"

/************************************************
 * Public Interface 
 ***********************************************/

/**
 * Initializes the chained hash table specified by htbl.
 *
 * @complexity O(m), where m is the number of buckets in the hash table.
 *
 * @param htbl 哈希表
 * @param buckets The number of buckets allocated in the hash table 
 * @param h user-defined hash function for hashing keys.
 * @param match user-defined function to determine whether two keys match, return 1 if key1 is equal to key2, and 0 otherwise
 * @param destroy free dunamically allocated data 
 *
 * @return 0 if initializing the hash table is successful, or -1 otherwise.
 *
 * */
Token lex(const char *istream, CHTbl *symtbl) {
    Token       token;
    Symbol      *symbol;
    int         length, retval, i;

    // Allocate space for a symbol 
    if ((symbol = (Symbol *)malloc(sizeof(Symbol))) == NULL)
        return error;

    // Process the next token.
    if ((symbol->lexeme = next_token(istream)) == NULL) {
        // Return that there is no more input.
        free(symbol);
        return lexit;
    }
    else {
        // Determine the token type.
        symbol->token = digit;
        length = strlen(symbol->lexeme);

        for (i = 0; i < length; i++) {
            if (!isdigit(symbol->lexeme[i]))
                symbol->token = other;
        }

        memcpy(&token, &symbol->token, sizeof(Token));

        // Insert the symbol into the symbol table.

        if ((retval = chtbl_insert(symtbl, symbol)) < 0) {
            free(symbol);
            return error;
        }
        else if (retval == 1) {
            // The stmbol is already in the symbol table.
            free(symbol);
        }
    }

    // Return the token for the parser.
    return token;
}
