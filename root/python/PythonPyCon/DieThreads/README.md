Die Threads
==========
    **When threads sleep do they dream?**
    **Why Choose Async?**
        The GIL : The Global Interpreter Lock 

.. code:: python3
    
"""
    bash % python3 hellothreads.py
    ^C ^C ^C ^Z 
    [1]+ Stopped /usr/local/bin/python3 hellothreads.py 
    bash % ps | grep python3 
    bash % kill -9 9822 
    [1]+ Killed: 9 /usr/local/bin/python3 hellothreads.py 
    bash %
"""
    
    **Born Under a Bad Sign**

.. code:: python3

    #!/usr/bin/env python3
    # -*- coding:utf-8 -*-
    import threading 

    t = threading.Thread(target=spam, args=(5,))
    t.start() 

    # OR 

    class MyThread(threading.Thread):
        def __init__(self, x):
            super().__init__()
            self.x = x 
        def run(self):
            spam(self.x)
    t = MyThread(5)
    t.start()

**Thread Cancellation**
    
