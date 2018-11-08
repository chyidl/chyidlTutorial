Keras + deep learning REST API
    Our Keras + deep learning REST API will be capable of batch processing images,scaling to multiple machines (including multiple web servers and Redis instances), and round-robin shceduling when placed behind a load balancer.

    Keras
    Redis (an in-memory data structure store)
    Flask (a micro web framework for Python)
    Message queuing and message broker programming paradigms


 Intro Tutorial
    the First discussion of the Redis data store and how it can be facilitate message queuing and message brokering.

    Then, configure Python development environment by installing the required Python packages to build our Keras deep learning REST API.

    the third, Using the Flask web framework, Redis and Flask servers, follow by submitting inference requests to our deep learning API endpoint using both cURL and Python.


 Intro Redis as a REST API message broker/message queue

    Redis is an in-memory data store, It is different than a simple key/value store (such as memcached) as it can store actual data structures.

    Using Redis as a message broker/message queue.
         Running Redis on our machine
         Queuing up data (images) to our Redis store to be processed by our REST API
         Polling Redis for new batches of input images
         Classifying the images and returning the results to the client.

    Configuring and installing Redis for our Keras REST API
         $ wget http://download.redis.io/redis-stable.tar.gz
         $ tar xvzf redis-stable.tar.gz
         $ cd redis-stable
         $ make
         $ sudo make install

         $ redis-server
         $ redis-cli ping

    Configuring your Python development environment to build a Keras REST API
         $ pip3 install numpy scipy h5py tensorflow keras flask gevent imutils requests redis Pillow

 Implementing a scalable Keras REST API


