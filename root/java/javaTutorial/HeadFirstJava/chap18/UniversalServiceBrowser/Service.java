/*
 * Service.java
 * UniversalServiceBrowser
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/15/19 10:06.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;
import java.io.*;

/**
 * Interface Service (What the GUI services implement)
 * */
public interface Service extends Serializable {
    public JPanel getGuiPanel();   
}

