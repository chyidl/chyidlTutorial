//
//  frames.c
//  MasterAlgorithmsWithC
//  Description - Frame Management
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdio.h>

#include "frames.h"
#include "list.h"

/***************************************************************
 *                                                              *
 * ----------------------- alloc_frame -------------------------*
 *                                                              *
 ***************************************************************/
int alloc_frame(List *frames) {
    int frame_number, *data;

    if (list_size(frames) == 0)
        // Return that there are no frames available.
        return -1;
    else {
        if (list_rem_next(frames, NULL, (void **)&data) != 0)
            // Return that a frame could not be retrieved 
            return -1;
        else {
            // Store the number of the available frame.
            frame_number = *data;
            free(data);

        }
    }

    return frame_number;
}

/***************************************************************
 *                                                              *
 * ----------------------- free_frame -------------------------*
 *                                                              *
 ***************************************************************/
int free_frame(List *frames, int frame_number) {
    int     *data;
    
    // Allocate storage for the frame number 
    if ((data = (int *)malloc(sizeof(int))) == NULL)
        return -1;

    // Put the frame back in the list of available frames.
    *data = frame_number;
    if (list_ins_next(frames, NULL, data) != 0)
        return -1;

    return 0;
}
