//
//  page.c
//  MasterAlgorithmsWithC
//  Description - Implementation of Second-Chance Page Replacement 
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include "clist.h"
#include "page.h"

/***************************************************************
 *                                                              *
 * ---------------------- replace_page -------------------------*
 *                                                              *
 ***************************************************************/
int replace_page(CListElmt **current) {
    // Circle through the list of pages until one is found to replace 
    while (((Page *)(*current)->data)->reference != 0) {
        ((Page *)(*current)->data)->reference = 0;
        *current = clist_next(*current);
    }
    return ((Page *)(*current)->data)->number;
}
