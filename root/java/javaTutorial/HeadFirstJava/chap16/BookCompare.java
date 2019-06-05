/*
 * BookCompare.java
 * chap16
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/05/19 10:16.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;

public class BookCompare implements Comparator<Book> {

    public int compare(Book one, Book two) {
        return (one.title.compareTo(two.title));
    }

}

